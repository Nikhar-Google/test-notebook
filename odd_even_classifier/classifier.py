
import tensorflow as tf
import numpy as np

class OddEvenClassifier:
    def __init__(self):
        """Initialize the classifier by building the model."""
        self.model = self._build_model()

    def _build_model(self):
        """Builds and compiles the TensorFlow model."""
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(8, activation='relu', input_shape=(1,)),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def train(self, epochs=100, verbose=1):
        """
        Trains the model on numbers 0-99 with labels for odd/even.
        
        Args:
            epochs (int): Number of training epochs.
            verbose (int): Verbosity mode. 0 = silent, 1 = progress bar, 2 = one line per epoch.
        """
        # Generate training data: numbers 0 to 99
        X = np.arange(100, dtype=np.float32).reshape(-1, 1)
        y = (X % 2).astype(np.float32)  # 0 for even, 1 for odd

        self.model.fit(X, y, epochs=epochs, verbose=verbose)

    def predict(self, numbers):
        """
        Predict whether numbers are odd or even.
        
        Args:
            numbers (int or list/array of int): A single number or list of numbers.
            
        Returns:
            A list of tuples (number, probability, label) where label is 'Odd' or 'Even'.
        """
        # Ensure the input is a numpy array with shape (n, 1)
        numbers_arr = np.atleast_1d(numbers).astype(np.float32).reshape(-1, 1)
        predictions = self.model.predict(numbers_arr)

        results = []
        for num, pred in zip(numbers_arr.flatten(), predictions):
            label = "Odd" if pred[0] > 0.5 else "Even"
            results.append((int(num), float(pred[0]), label))
        return results
