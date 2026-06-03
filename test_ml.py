import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import(train_model, inference, compute_model_metrics,)

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Test to confirm the model is using RandomForestClassifier.
    """
    # Your code here
    X = np.array([[1,2], [3,4], [5,6], [7,8]])
    y = np.array([0, 1, 0, 1])

    model = train_model(X,y)
    assert isinstance(model, RandomForestClassifier)
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Test to confirm the model inference returns expected output size.
    """
    # Your code here
    X = np.array([[1,2], [3,4], [5,6], [7,8]])
    y = np.array([0, 1, 0, 1])

    model = train_model(X,y)
    preds = inference(model, X)
    assert len(preds) == len(X)
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Test to confirm the model returns the expected metrics.
    """
    # Your code here
    y_true = np.array([1, 1, 0, 0])
    y_pred = np.array([1, 0, 0, 0])

    precision, recall, fbeta = compute_model_metrics(
        y_true, y_pred
    )

    assert round(precision, 2) == 1.00
    assert round(recall, 2) == 0.50
    assert round(fbeta, 2) == 0.67
    pass
