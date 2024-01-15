import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(data, test_size=0.2, random_state=42):
    """
    Split the data into train and test sets.

    Args:
        data (pd.DataFrame): Input data.
        test_size (float): Proportion of data to include in the test set.
        random_state (int): Random seed for reproducibility.

    Returns:
        pd.DataFrame, pd.DataFrame: Train and test sets.
    """
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
    return train_data, test_data


def remove_nan_rows(data):
    """
    Remove rows that contain NaN values in the columns: 'age', 'gender', 'ethnicity'.

    Args:
        data (pd.DataFrame): Input data.

    Returns:
        pd.DataFrame: Data with NaN rows removed.
    """
    data = data.dropna(subset=['age', 'gender', 'ethnicity'])
    return data


def fill_nan_with_mean(data):
    """
    Fill NaN with the mean value of the column in the columns: 'height', 'weight'.

    Args:
        data (pd.DataFrame): Input data.

    Returns:
        pd.DataFrame: Data with NaNs filled with mean values.
    """
    data['height'].fillna(data['height'].mean(), inplace=True)
    data['weight'].fillna(data['weight'].mean(), inplace=True)
    return data


def generate_dummies_for_ethnicity(data):
    """
    Generate dummies for the 'ethnicity' column (One hot encoding).

    Args:
        data (pd.DataFrame): Input data.

    Returns:
        pd.DataFrame: Data with ethnicity dummies.
    """
    data = pd.get_dummies(data, columns=['ethnicity'], prefix='ethnicity')
    return data


def create_binary_gender_variable(data):
    """
    Create a binary variable for 'gender' M/F.

    Args:
        data (pd.DataFrame): Input data.

    Returns:
        pd.DataFrame: Data with the binary gender variable.
    """
    data['gender'] = data['gender'].apply(lambda x: 1 if x == 'M' else 0)
    return data
