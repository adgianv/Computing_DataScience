import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    """
    Data_loader class for loading and splitting data.

    Attributes:
        filename (str): Path to the CSV data file.

    Methods:
        load_and_split_data(self, test_size=0.2, random_state=42)
            Loads and splits the data into train and test sets.
    """

    def __init__(self, filename):
        self.filename = filename

    def load_and_split_data(self, test_size=0.2, random_state=42):
        data = pd.read_csv(self.filename)
        train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
        return train_data, test_data


class NanRemover:
    """
    NaN_remover class for removing NaN rows from data.

    Attributes:
        data (pd.DataFrame): Input data.

    Methods:
        remove_nan(self, cols)
            Removes NaN rows from data based on specified columns.
    """

    def __init__(self, data):
        self.data = data

    def remove_nan(self, cols: list):
        data = self.data.dropna(subset=cols)
        return data


class NanImputer:
    """
    NaN_imputer class for filling NaN values in data with mean.

    Attributes:
        data (pd.DataFrame): Input data.

    Methods:
        fill_nan(self, cols)
            Fills NaN values in data with mean based on specified columns.
    """

    def __init__(self, data):
        self.data = data

    def fill_nan(self, cols):
        for col in cols:
            self.data[col].fillna(self.data[col].mean(), inplace=True)
        return self.data