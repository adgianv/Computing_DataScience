import pandas as pd


def load_data(filename):
    """
    Load data from a CSV file and return a DataFrame.

    Args:
        filename (str): Path to the CSV data file.

    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    try:
        data = pd.read_csv(filename)
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None
