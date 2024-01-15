from abc import ABC, abstractmethod
import numpy as np

class Feature(ABC):
    """
    An abstract class for feature transformation.
    """
    
    @abstractmethod
    def transform(self):
        raise NotImplementedError

class Standardizer(Feature):
    """
    Standardizer class standardizes specified columns in the dataset.

    Attributes:
        data (pd.DataFrame): Dataframe containing data of interest.

    Methods:
        transform(self, cols)
            Standardizes specified columns in the provided dataset.
    """
    def __init__(self, data):
        self.data = data

    def transform(self, cols):
        for i in cols:
            self.data[i] = (self.data[i] - np.mean(self.data[i])) / np.std(self.data[i])

class Normalizer(Feature):
    """
    Normalizer class normalizes specified columns in the dataset.

    Attributes:
        data (pd.DataFrame): Dataframe containing data of interest.

    Methods:
        transform(self, cols)
            Normalizes specified columns in the provided dataset and returns the normalized data.
    """
    def __init__(self, data):
        self.data = data

    def transform(self, cols):
        for i in cols:
            min_value = min(self.data[i])
            max_value = max(self.data[i])
            normalized_column = []

            for value in self.data[i]:
                normalized_value = (value - min_value) / (max_value - min_value)
                normalized_column.append(normalized_value)
            self.data[i] = normalized_column
        return self.data









