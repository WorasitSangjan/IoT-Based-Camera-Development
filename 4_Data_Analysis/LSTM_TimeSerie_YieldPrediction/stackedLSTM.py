from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Input, Dropout, BatchNormalization, Masking
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2

from MachineLearningModule.LSTM.lstm_model import LSTMModel


class StackedLSTM(LSTMModel):
    def __init__(self, num_epochs: int = 300, verbose: int = 1):
        super().__init__(num_epochs, verbose)

    def build_model(self, n_steps):
        self.model = Sequential()
        self.model.add(Input(shape=(n_steps, self.n_features)))
        self.model.add(Masking(mask_value=0.0))
        self.model.add(LSTM(50, activation='relu', return_sequences=True, kernel_regularizer=l2(0.01)))
        self.model.add(Dropout(0.2))
        self.model.add(BatchNormalization())
        self.model.add(LSTM(50, activation='relu', kernel_regularizer=l2(0.01)))
        self.model.add(Dropout(0.2))
        self.model.add(BatchNormalization())
        self.model.add(Dense(1, kernel_regularizer=l2(0.01)))
        optimizer = Adam(learning_rate=0.0005)
        self.model.compile(optimizer=optimizer, loss='mse')
