 # LSTM models for yield prediction on AGIcam time series data
 # Author: Trevor Buchanan and Worasit Sangjan
 # Date: April 2024

import numpy as np
from Helpers.utility import shuffle_in_unison
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Input, Dropout, BatchNormalization, Masking
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import EarlyStopping
from MachineLearningModule.data_handler import prep_sequences_target_val


class LSTMModel:
    """Base class for LSTM models used in crop yield prediction"""
    
    def __init__(self, num_epochs: int = 500, verbose: int = 1) -> None:
        self.num_epochs = num_epochs
        self.verbose = verbose
        self.model = None
        self.n_features = 1

    def load_trained_model(self, model_num):
        """Load a previously saved model"""
        model_path = f'MachineLearningModule/LSTM/SavedModels/model_{model_num}.keras'
        self.model = load_model(model_path)

    def save_trained_model(self, model_num):
        """Save the current trained model"""
        model_path = f'MachineLearningModule/LSTM/SavedModels/model_{model_num}.keras'
        self.model.save(model_path)

    def build_model(self, n_steps):
        """
        Build the LSTM model architecture
        
        Args:
            n_steps: Number of time steps in input sequences
            
        Note: This method should be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement build_model method")

    def train(self, training_sequences: list[list], target_values: list[float]) -> None:
        """
        Train the LSTM model on given training data
        
        Args:
            training_sequences: List of multivariate sequences for training
            target_values: List of target crop yield values
        """
        # Prepare sequences for training
        sets, target_outs = prep_sequences_target_val(training_sequences, target_values, 2)
        sets, target_outs = shuffle_in_unison(sets, target_outs)
        
        # Get input dimensions
        n_steps = sets.shape[0]
        self.n_features = len(training_sequences[0])
        
        print(f'Average target: {sum(target_outs) / len(target_outs)}')
        
        # Build model if not already built
        if self.model is None:
            self.build_model(n_steps)
        
        # Set up early stopping callback
        early_stopping = EarlyStopping(
            monitor='val_loss', 
            patience=75, 
            restore_best_weights=True
        )
        
        # Train the model
        self.model.fit(
            sets, target_outs,
            epochs=self.num_epochs,
            verbose=self.verbose,
            validation_split=0.2,
            callbacks=[early_stopping]
        )

    def predict(self, sequence: np.array) -> float:
        """
        Make a prediction for a given input sequence
        
        Args:
            sequence: Input sequence for prediction
            
        Returns:
            Predicted crop yield value
        """
        self.n_features = sequence[0].size
        sequence = np.array([sequence])
        predicted = self.model.predict(sequence, verbose=self.verbose)
        return predicted[0][0]


class VanillaLSTM(LSTMModel):
    """Single-layer LSTM model for crop yield prediction"""
    
    def __init__(self, num_epochs: int = 300, verbose: int = 1):
        super().__init__(num_epochs, verbose)

    def build_model(self, n_steps):
        """Build a vanilla (single-layer) LSTM model"""
        self.model = Sequential()
        
        # Input layer
        self.model.add(Input(shape=(n_steps, self.n_features)))
        
        # Masking layer to handle padded sequences
        self.model.add(Masking(mask_value=0.0))
        
        # LSTM layer
        self.model.add(LSTM(100, activation='relu', kernel_regularizer=l2(0.01)))
        
        # Regularization layers
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.2))
        
        # Output layer
        self.model.add(Dense(1))
        
        # Compile model
        optimizer = Adam(learning_rate=0.0005)
        self.model.compile(optimizer=optimizer, loss='mse')


class StackedLSTM(LSTMModel):
    """Multi-layer (stacked) LSTM model for crop yield prediction"""
    
    def __init__(self, num_epochs: int = 300, verbose: int = 1):
        super().__init__(num_epochs, verbose)

    def build_model(self, n_steps):
        """Build a stacked (multi-layer) LSTM model"""
        self.model = Sequential()
        
        # Input layer
        self.model.add(Input(shape=(n_steps, self.n_features)))
        
        # Masking layer to handle padded sequences
        self.model.add(Masking(mask_value=0.0))
        
        # First LSTM layer (returns sequences for next LSTM layer)
        self.model.add(LSTM(50, activation='relu', return_sequences=True, kernel_regularizer=l2(0.01)))
        self.model.add(Dropout(0.2))
        self.model.add(BatchNormalization())
        
        # Second LSTM layer (final LSTM layer)
        self.model.add(LSTM(50, activation='relu', kernel_regularizer=l2(0.01)))
        self.model.add(Dropout(0.2))
        self.model.add(BatchNormalization())
        
        # Output layer
        self.model.add(Dense(1, kernel_regularizer=l2(0.01)))
        
        # Compile model
        optimizer = Adam(learning_rate=0.0005)
        self.model.compile(optimizer=optimizer, loss='mse')