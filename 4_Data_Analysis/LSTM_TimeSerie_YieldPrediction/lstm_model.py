import numpy as np

from Helpers.utility import shuffle_in_unison

from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping

from MachineLearningModule.data_handler import prep_sequences_target_val


class LSTMModel:
    def __init__(self, num_epochs: int = 500, verbose: int = 1) -> None:
        self.num_epochs = num_epochs
        self.verbose = verbose
        self.model = None
        self.n_features = 1

    def load_trained_model(self, model_num):
        self.model = load_model(f'MachineLearningModule/LSTM/SavedModels/model_{model_num}.keras')

    def save_trained_model(self, model_num):
        self.model.save(f'MachineLearningModule/LSTM/SavedModels/model_{model_num}.keras')

    def build_model(self, n_steps):
        """
        Builds an LSTM model
        :param n_steps: int - Size of input shape (features=1 because only predicting one value)
        :return: keras.models.Sequential - New built LSTM model
        """
        raise NotImplementedError("No build_model function implemented")

    def train(self, training_sequences: list[list], target_values: list[float]) -> None:
        """
        Used to train LSTM on given training sequences targeting corresponding given target values
        :param training_sequences: list[list] - list of sequences that correspond to a target output in target_values
        :param target_values: list[float] - list of target values that lstm tries to train towards
        :return: None
        """
        sets, target_outs = prep_sequences_target_val(training_sequences, target_values, 2)
        sets, target_outs = shuffle_in_unison(sets, target_outs)
        n_steps = sets.shape[0]
        self.n_features = len(training_sequences[0])
        print(f'Avg target: {sum(target_outs) / len(target_outs)}')
        # Define model
        if self.model is None:
            self.build_model(n_steps)
        # Early stopping
        early_stopping = EarlyStopping(monitor='val_loss', patience=75, restore_best_weights=True)
        # Fit model with validation split
        self.model.fit(sets, target_outs, epochs=self.num_epochs, verbose=self.verbose,
                       validation_split=0.2, callbacks=[early_stopping])

    def predict(self, sequence: np.array) -> float:
        """
        Function to be called to get predicted value after training
        :param sequence: list - Sequence of numbers to be tested and predicted for
        :return: float - Result of running the input sequence through the LSTM model
        """
        self.n_features = sequence[0].size
        sequence = np.array([sequence])
        predicted = self.model.predict(sequence, verbose=self.verbose)
        return predicted[0][0]
