from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

def features_and_target_split(data, features, target):
    """
    Split the data frame into features and target variable.

    Args:
        data (pd.DataFrame): Input data.
        features (list): list of the column names of the features of the data.
        target (string): target variable column name.

    Returns:
        pd.DataFrame, pd.DataFrame: features variables and target variable dataframes.
    """
    X, y = data[features], data[target]
    return X, y


def train_model(X_train, y_train, X_test):
    """
    Trains the model.

    Args:
        X_train (pd.DataFrame): Features of the train data.
        y_train (pd.DataFrame): target variable of train data.
        X_test (pd.DataFrame): Features of the test data.

    Returns:
        list, list: predictions for train and test data.
    """
    model = LogisticRegression()
    model.fit(X_train, y_train)

    train_probs = model.predict_proba(X_train)[:, 1]
    test_probs = model.predict_proba(X_test)[:, 1]

    return train_probs, test_probs



def evaluation(y_train, y_test, train_probs, test_probs):
    """
    Trains the model.

    Args:
        y_train (pd.DataFrame): target variable of train data.
        y_test (pd.DataFrame): target variable of test data.
        train_probs (float): prediction of the train data.
        test_probs (float): prediction of the train data.

    Returns:
        float, float: scores for the predictions for train and test data.
    """
    roc_auc_train = roc_auc_score(y_train, train_probs)
    roc_auc_test = roc_auc_score(y_test, test_probs)

    return roc_auc_train, roc_auc_test

