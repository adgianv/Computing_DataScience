from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

class Model:
    """
    Model class for training and predicting using a machine learning model.

    Attributes:
        _features (list): List of feature columns used for training and prediction.
        _target (str): Target column used for training and prediction.
        model: Machine learning model for training and prediction.

    Methods:
        __init__(self, features, target, hyperparameters=None)
            Initializes the Model class with the specified parameters.

        train(self, df_train)
            Trains the model using the provided training data.

        predict(self, data)
            Predicts using the trained model on the provided data and returns predicted probabilities.

        accuracy(self, data, pred_col)
            Reports accuracy of predictions.
    """
    def __init__(self, features, target, hyperparameters=None):
        """
        Initializes the Model class with the specified parameters.

        Args:
            features (list): List of feature columns used for training and prediction.
            target (str): Target column used for training and prediction.
            hyperparameters (dict): Optional dictionary of hyperparameters for the model.
        """
        self._features = features
        self._target = target
        self.model = RandomForestClassifier(**hyperparameters) if hyperparameters else RandomForestClassifier()

    def train(self, df_train):
        """
        Trains the model using the provided training data.

        Args:
            df_train (pd.DataFrame): DataFrame to train.
        """
        self.model.fit(df_train[self._features], df_train[self._target])
    
    def predict(self, data):
        """
        Predicts using the trained model on the provided data and returns predicted probabilities.

        Args:
            data (pd.DataFrame): DataFrame to test.

        Returns:
            (ndarray): Class probabilities of the input sample.
        """
        X_test = data[self._features]
        return self.model.predict_proba(X_test)[:, 1]
    
    def accuracy(self, data, pred_col):
        """
        Reports accuracy of predictions.

        Args:
            data (pd.DataFrame): DataFrame containing target value and predictions.
            pred_col (str): Name of predictions column.

        Returns:
            (float): Accuracy score.
        """
        return roc_auc_score(data[self._target], data[pred_col])