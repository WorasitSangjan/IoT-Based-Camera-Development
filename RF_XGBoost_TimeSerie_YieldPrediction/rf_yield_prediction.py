import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, LeaveOneOut
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import logging
import matplotlib.pyplot as plt

# Set up logging with both file and console output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("crop_prediction.log"),
        logging.StreamHandler()
    ]
)

# Function to calculate AUC
def calculate_auc(group):
    group = group.sort_values(by='date')
    timepoints = group['date'].astype('int64') // 10**9
    values = group['mean'].values
    return np.trapz(values, x=timepoints)

def main():
    try:
        # Load dataset
        data_path = r'/Users/ws/Library/CloudStorage/OneDrive-Personal/Paper_IoT/Winter_Wheat/Code/2_segmented_data.csv'
        data = pd.read_csv(data_path)
        data['date'] = pd.to_datetime(data['date'])

        # Adjust interval calculation
        data['interval'] = ((data['date'] - data['date'].min()).dt.days - 7) // 3
        data = data[data['interval'] >= 0]  # Ensure intervals start at 7 days

        # Calculate AUC for each combination
        auc_data = data.groupby(['variety', 'rep_var', 'vi', 'interval']).apply(calculate_auc).reset_index(name='AUC')

        # Pivot data
        pivot_data = auc_data.pivot_table(
            index=['variety', 'rep_var', 'interval'],
            columns='vi',
            values='AUC'
        ).reset_index()

        # Merge yield values
        yield_mapping = data[['variety', 'rep_var', 'kg/ha']].drop_duplicates()
        pivot_data = pd.merge(pivot_data, yield_mapping, on=['variety', 'rep_var'], how='left')
        pivot_data.rename(columns={'kg/ha': 'yield'}, inplace=True)

        # Define hyperparameter grid
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }

        # Run the loop 10 times
        overall_results = []
        overall_feature_importance = []

        for loop in range(10):
            logging.info(f"Starting loop {loop + 1} of 10")

            # Initial storage for interval-level metrics and feature importance 
            results_all_intervals = []
            feature_importance_all_intervals = []

            # Loop through each interval
            for interval in sorted(pivot_data['interval'].unique()):
                logging.info(f"Evaluating for interval: {interval}")

                # Filter data for the current interval 
                interval_data = pivot_data[pivot_data['interval'] == interval]
                X = interval_data.drop(columns=['variety', 'rep_var', 'interval', 'yield'])
                y = interval_data['yield']

                # Skip if not enough data for LOOV
                if len(X) <= 1:
                    logging.warning(f"Skipping interval {interval} due to insufficient data.")
                    continue

                # Leave-One-Out Cross-Validation
                loo = LeaveOneOut()
                y_true_all, y_pred_all = [], []
                interval_feature_importance = pd.DataFrame(index=X.columns)

                for train_idx, test_idx in loo.split(X):
                    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
                    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

                    # Hyperparameter tuning for the current test row 
                    model = RandomForestRegressor(bootstrap=True)  # Default Random Forest with no random_state
                    grid_search = GridSearchCV(model, param_grid, cv=3, scoring='neg_mean_squared_error', n_jobs=-1)
                    grid_search.fit(X_train, y_train)

                    # Best parameter for this test row
                    best_model = grid_search.best_estimator_

                    # Predict yield for the test row 
                    y_pred = best_model.predict(X_test)[0]
                    y_true_all.append(y_test.values[0])
                    y_pred_all.append(y_pred)

                    # Extract feature importance and store
                    feature_importance = best_model.feature_importances_
                    interval_feature_importance[f"fold_{len(y_true_all)}"] = feature_importance

                # Aggregate feature importance for the interval 
                interval_feature_importance['mean_importance'] = interval_feature_importance.mean(axis=1)
                interval_feature_importance['interval'] = interval
                feature_importance_all_intervals.append(interval_feature_importance.reset_index())

                # Calculate metrics for the interval 
                rmse = np.sqrt(mean_squared_error(y_true_all, y_pred_all))
                mae = mean_absolute_error(y_true_all, y_pred_all)
                mape = np.mean(np.abs((np.array(y_true_all) - np.array(y_pred_all)) / np.array(y_true_all))) * 100 
                r2 = r2_score(y_true_all, y_pred_all)

                results_all_intervals.append({
                    'interval': interval,
                    'rmse': rmse,
                    'mae': mae,
                    'mape': mape,
                    'r2': r2
                })

            # Append the results of the current loop
            overall_results.append(pd.DataFrame(results_all_intervals))
            overall_feature_importance.append(pd.concat(feature_importance_all_intervals, ignore_index=True))

        # Aggregate the results across all loops
        final_results = pd.concat(overall_results)
        summary_metrics = final_results.groupby('interval').agg(['mean', 'std'])

        # Save aggregated results
        summary_metrics.to_csv('aggregated_interval_metrics_rf.csv')
        logging.info("Aggregated results saved to 'aggregated_interval_metrics_rf.csv'")

        # Save aggregated feature importance
        final_feature_importance = pd.concat(overall_feature_importance, ignore_index=True)
        final_feature_importance.to_csv('aggregated_feature_importance_rf.csv', index=False)
        logging.info("Aggregated feature importance saved to 'aggregated_feature_importance_rf.csv'")

        # Create and save visualization of results
        plt.figure(figsize=(15, 10))
        metrics = ['rmse', 'mae', 'mape', 'r2']
        for i, metric in enumerate(metrics, 1):
            plt.subplot(2, 2, i)
            mean_values = summary_metrics[(metric, 'mean')]
            std_values = summary_metrics[(metric, 'std')]
            intervals = mean_values.index
            
            plt.errorbar(intervals, mean_values, yerr=std_values, fmt='o-', capsize=5)
            plt.title(f'{metric.upper()} by Interval')
            plt.xlabel('Interval')
            plt.ylabel(metric.upper())
        
        plt.tight_layout()
        plt.savefig('metrics_with_uncertainty.png')
        plt.close()
        
        logging.info("Analysis completed successfully")
        
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()