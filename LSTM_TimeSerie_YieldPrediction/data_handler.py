import numpy as np
import ast
import random
import heapq
from Helpers.utility import get_plot, percent_error
from DataStructures.plot import Plot

def prep_sequences_target_val(sequences: list[list], targets: list[float], know_threshold: int) \
        -> tuple[np.array, np.array]:
    """Split the data into sets of length n_steps and have their target always be yield"""
    def pad_list(lst, pad_left, pad_right, num):
        total_length = len(lst) + pad_left + pad_right
        padded_array = np.full(total_length, num, dtype=float)
        padded_array[pad_left:pad_left + len(lst)] = lst
        return padded_array.tolist()

    max_len = 0
    for seq in sequences:
        if len(seq[0]) > max_len:
            max_len = len(seq[0])

    num_features = len(sequences[0])
    sets = []
    target_outputs = []
    for plot_sequences, target in zip(sequences, targets):
        plot_step_list_seqs = {}
        plot_step_list_targets = []
        for j, variate_sequence in enumerate(plot_sequences):
            end_i_set = len(variate_sequence)
            for i, _ in enumerate(variate_sequence):
                if end_i_set - i < know_threshold:  # Stop adding to the set when past know threshold
                    break
                seq_set, seq_target_output = variate_sequence[0:end_i_set - i], target
                seq_set = pad_list(seq_set, 0, i, 0)
                if end_i_set < max_len:
                    ignore_padding_len = max_len - end_i_set
                    seq_set = pad_list(seq_set, 0, ignore_padding_len, 0)
                if j == 0:
                    plot_step_list_targets.append(seq_target_output)
                if i not in plot_step_list_seqs.keys():
                    plot_step_list_seqs[i] = []
                plot_step_list_seqs[i].append(seq_set)

        sets.append(list(plot_step_list_seqs.values()))
        target_outputs.append(plot_step_list_targets)

    # if num_features == 1:  # Uni-variate
    #     a, b = np.array(sets), np.array(target_outputs)
    #     a = a.reshape((a.shape[0], a.shape[1], num_features))
    # else:  # Multivariate
    full_sets = []
    full_targets = []
    for plot_sets, plot_targets in zip(sets, target_outputs):
        for know_day_set, know_day_target in zip(plot_sets, plot_targets):
            know_day_array = np.array(know_day_set)
            know_day_array_t = know_day_array.T
            full_sets.append(know_day_array_t)
            full_targets.append(know_day_target)
    a = np.array(full_sets)
    b = np.array(full_targets)
    return a, b


class DataHandler:
    def __init__(self, plots: list[Plot]) -> None:
        self.plots = plots
        self.training_sets: list[tuple[list, int, int]] = []
        self.testing_sets: list[tuple[list, int, int]] = []
        self.predictions: list[tuple[list, int, int, float]] = []
        self.accuracies: list[tuple[list, int, int]] = []
        self.best_accuracies_dates: list[int] = []
        self.accuracies_at_bests: list[float] = []
        self.num_buckets = 7

    def make_sets(self, target_variates: list[str], training_percentage_amt: int, cut_sets=False,
                  bulk_sets=False) -> None:
        """Makes a set of uni-variate training and testing sets with given target variate and saves """
        total_amt = len(self.plots)
        unique_count = int(total_amt * (training_percentage_amt / 100))
        test_plot_indices = set()

        while len(test_plot_indices) < unique_count:
            index = random.randint(0, total_amt - 1)
            test_plot_indices.add(index)

        test_plot_indices = list(test_plot_indices)
        if len(test_plot_indices) == 0:
            test_plot_indices.append(random.randint(0, total_amt - 1))
        # Make training sets
        for i, plot in enumerate(self.plots):
            multi_var_set = []
            for target_variate in target_variates:
                uni_var_set = self.get_set(plot, target_variate)
                if len(uni_var_set) > 0:
                    if i in test_plot_indices:  # Check if in 80 percent group of test plots
                        multi_var_set.append(uni_var_set)
                    else:
                        multi_var_set.append(uni_var_set)
            if i in test_plot_indices:
                self.training_sets.append((multi_var_set, plot.variety_index, plot.replication_variety))
            else:
                self.testing_sets.append((multi_var_set, plot.variety_index, plot.replication_variety))

        if cut_sets:
            self.cut_sets_to_level()
        if bulk_sets:
            self.bulk_sets_to_level()
        print(f'Number of training sets: {len(self.training_sets)}')
        print(f'Number of testing sets: {len(self.testing_sets)}')

    def save_sets(self, model_num: int) -> None:
        """Saves the testing and training data to respective files"""
        test_file_path = f'MachineLearningModule/SavedDataForModels/saved_test_data_{model_num}.txt'
        with open(test_file_path, 'w') as file:
            for tup in self.testing_sets:
                line = ', '.join(map(str, tup))
                file.write(line + '\n')

        training_file_path = f'MachineLearningModule/SavedDataForModels/saved_training_data_{model_num}.txt'
        with open(training_file_path, 'w') as file:
            for tup in self.training_sets:
                line = ', '.join(map(str, tup))
                file.write(line + '\n')

    def load_saved_sets(self, max_training_data_amt: int, model_num: int) -> None:
        """Loads saved testing and training data from their respective files"""
        test_file_path = f'MachineLearningModule/SavedDataForModels/saved_test_data_{model_num}.txt'
        with open(test_file_path, 'r') as file:
            for line in file:
                tuple_str = line.strip()
                parsed_tuple = ast.literal_eval(tuple_str)
                self.testing_sets.append(parsed_tuple)

        amt = 0
        training_file_path = f'MachineLearningModule/SavedDataForModels/saved_training_data_{model_num}.txt'
        with open(training_file_path, 'r') as file:
            for line in file:
                if amt >= max_training_data_amt:
                    break
                tuple_str = line.strip()
                parsed_tuple = ast.literal_eval(tuple_str)
                self.training_sets.append(parsed_tuple)
                amt += 1
        print(f'Number of training sets: {len(self.training_sets)}')
        print(f'Number of testing sets: {len(self.testing_sets)}')

    def clear_predictions(self) -> None:
        """Clears the predictions and accuracies"""
        self.predictions.clear()
        self.accuracies.clear()
        self.best_accuracies_dates.clear()
        self.accuracies_at_bests.clear()

    @staticmethod
    def get_set(plot: Plot, target_variate: str) -> list:
        """Get a list of values of given plot, and target variate"""
        uni_variate_set = []
        for dp in plot.data_points:
            value = getattr(dp.vi_state, target_variate, None)
            if value is None:
                value = getattr(dp.conditions_state, target_variate, None)
            if value is not None:
                uni_variate_set.append(value)
        return uni_variate_set

    def train_on_training_sets(self, model) -> None:
        """Train given model on class's training sets"""
        if not self.training_sets:
            print("No existing training sets found")
            return
        training_sets = []
        targets = []
        for training_set in self.training_sets:
            training_sets.append(training_set[0])
            targets.append(get_plot(training_set[1], training_set[2], self.plots).crop_yield)

        model.train(training_sets, targets)

    def make_predictions_and_accuracies_for_test_sets(self, model) -> None:
        """Populate self's list of predictions for test sets (also populates accuracies)"""
        if not self.testing_sets:
            print("No existing testing sets found")
            return
        self.clear_predictions()
        for test_set in self.testing_sets:
            test_sets_for_each_day, _ = prep_sequences_target_val([test_set[0]], [0 for _, _ in enumerate(test_set)], 0)
            predictions = []
            accuracies = []
            test_plot = get_plot(test_set[1], test_set[2], self.plots)
            expected = test_plot.crop_yield
            start_date = test_plot.data_points[0].date
            end_date = test_plot.data_points[len(test_plot.data_points) - 1].date
            date_range = end_date - start_date + 1
            dates = [start_date + i for i in range(date_range)]
            for t_set in reversed(test_sets_for_each_day):
                prediction = model.predict(t_set)
                predictions.append(prediction)
                accuracies.append(percent_error(prediction, expected))
            self.predictions.append((predictions, test_set[1], test_set[2], expected))
            self.accuracies.append((accuracies, test_set[1], test_set[2]))
            self.best_accuracies_dates.append(dates[accuracies.index(min(accuracies))])
            self.accuracies_at_bests.append(min(accuracies))

    def make_predictions_and_accuracies_for_training_sets(self, model) -> None:
        """Populate self's list of predictions for test sets (also populates accuracies)"""
        if not self.training_sets:
            print("No existing training sets found")
            return
        self.clear_predictions()
        for test_set in self.training_sets:
            test_sets_for_each_day, _ = prep_sequences_target_val([test_set[0]], [0 for _, _ in enumerate(test_set)], 0)
            predictions = []
            accuracies = []
            test_plot = get_plot(test_set[1], test_set[2], self.plots)
            expected = test_plot.crop_yield
            start_date = test_plot.data_points[0].date
            end_date = test_plot.data_points[len(test_plot.data_points) - 1].date
            date_range = end_date - start_date + 1
            dates = [start_date + i for i in range(date_range)]
            for t_set in reversed(test_sets_for_each_day):
                prediction = model.predict(t_set)
                predictions.append(prediction)
                accuracies.append(percent_error(prediction, expected))
            self.predictions.append((predictions, test_set[1], test_set[2], expected))
            self.accuracies.append((accuracies, test_set[1], test_set[2]))
            self.best_accuracies_dates.append(dates[accuracies.index(min(accuracies))])
            self.accuracies_at_bests.append(min(accuracies))

    def cut_sets_to_level(self):
        """Balances the distribution of crop yields across the training sets by moving some sets to the testing sets"""
        yields = []
        for tup in self.training_sets:
            yields.append(get_plot(tup[1], tup[2], self.plots).crop_yield)

        min_val = min(yields)
        max_val = max(yields)
        num_buckets = 7
        buckets = [0] * num_buckets
        for tup in self.training_sets:
            buckets[self.get_bucket_index(get_plot(tup[1], tup[2], self.plots).crop_yield,
                                          min_val, max_val, num_buckets)] += 1
        min_amt = min(buckets)
        to_rmv = []
        for tup in self.training_sets:
            index = self.get_bucket_index(get_plot(tup[1], tup[2], self.plots).crop_yield,
                                          min_val, max_val, num_buckets)
            if buckets[index] > min_amt:
                to_rmv.append(tup)
                buckets[index] -= 1

        for rmv in to_rmv:
            self.training_sets.remove(rmv)
            self.testing_sets.append(rmv)

    def bulk_sets_to_level(self):
        """Balances the distribution of crop yields across the training sets by fabricating new sets"""
        yields = []
        for tup in self.training_sets:
            yields.append(get_plot(tup[1], tup[2], self.plots).crop_yield)

        min_val = min(yields)
        max_val = max(yields)
        buckets = [0] * self.num_buckets
        for tup in self.training_sets:
            buckets[self.get_bucket_index(get_plot(tup[1], tup[2], self.plots).crop_yield,
                                          min_val, max_val, self.num_buckets)] += 1
        to_add = []
        max_amt = max(buckets)
        for tup in self.training_sets:
            index = self.get_bucket_index(get_plot(tup[1], tup[2], self.plots).crop_yield,
                                          min_val, max_val, self.num_buckets)
            amt = buckets[index]
            if amt < max_amt:
                for _ in range(max_amt - amt):
                    to_add.append(self.fabricate_set(tup))
                    buckets[index] += 1

        for add in to_add:
            self.training_sets.append(add)

    @staticmethod
    def fabricate_set(original_set: tuple[list, int, int], max_deviation: float = 0.01) -> tuple[list, int, int]:
        """Fabricates a new set by slightly modifying the values of the original set within a specified deviation range"""
        new_multi_set = []
        for orig_uni_set in original_set[0]:
            new_uni_set = []
            for uni_val in orig_uni_set:
                new_uni_set.append(uni_val + random.uniform(-max_deviation, max_deviation))
            new_multi_set.append(new_uni_set)
        return new_multi_set, original_set[1], original_set[2]

    @staticmethod
    def get_bucket_index(num: float, min_value: float, max_value: float, num_buckets: int) -> int:
        """Calculates the bucket index for a given number within a specified range and number of buckets"""
        bucket_range = (max_value - min_value) / num_buckets
        if bucket_range == 0:  # All numbers are the same
            return 0
        bucket_index = int((num - min_value) / bucket_range)
        # Make sure the last bucket includes the max_value
        if bucket_index == num_buckets:
            bucket_index -= 1
        return bucket_index