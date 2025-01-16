"""
Python Essentials for AI Assignment

This assignment covers key Python essentials for AI, including a refresher on Python for AI applications,
data handling and preprocessing, and implementing basic AI algorithms.

Before starting, ensure you have the following libraries installed:
- numpy
- pandas

You can install them using pip:
pip install numpy pandas
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from scipy.stats import zscore

def filter_outliers(data):
    """
    Filter outliers from a dataset. An outlier is defined as a value that is more than 2 standard deviations from the mean.

    Parameters:
    data (numpy.ndarray): 1D array containing numerical data.

    Returns:
    filtered_data (numpy.ndarray): The dataset with outliers removed.
    """
    filtered_data = []

    mean = np.mean(data)
    std = np.std(data)
    
    for value in data:
        if not (value < mean - (2 * std) or value > mean + (2 * std)):
            filtered_data.append(value)

    return filtered_data

def normalize_features(X):
    """
    Normalize the features in a dataset to have zero mean and unit variance.

    Parameters:
    X (numpy.ndarray): 2D array where each row represents a sample and each column represents a feature.

    Returns:
    normalized_X (numpy.ndarray): The dataset with normalized features.
    """
    
    normalized_X = []

    for feature in X:
        mean = np.mean(feature)
        std_dev = np.std(feature) 

        arr = []
        for value in feature:
            arr.append((value - mean) / std_dev) 
        normalized_X.append(arr)
    
    # Return array transposed to fit the format.
    return np.array(normalized_X).T


def implement_knn(X_train, y_train, X_test, k):
    """
    Implement the k-Nearest Neighbors (kNN) algorithm from scratch. Use Euclidean distance to find the k nearest neighbors.

    Parameters:
    X_train (numpy.ndarray): 2D array of training data samples.
    y_train (numpy.ndarray): 1D array of labels corresponding to the training samples.
    X_test (numpy.ndarray): 2D array of test data samples.
    k (int): The number of nearest neighbors to consider for making predictions.

    Returns:
    predictions (numpy.ndarray): Predicted labels for the test data.
    """
    predictions = []
    for test_sample in X_test:
        distances = np.linalg.norm(X_train - test_sample, axis = 1)

        # Retrieve the labels of the k nearest neighbors using the indices of the smallest k distance.
        k_nearest_labels = y_train[np.argsort(distances)[:k]]

        # Determine the most common label among the k nearest neighbors
        unique, counts = np.unique(k_nearest_labels, return_counts = True)
        label = unique[np.argmax(counts)]

        predictions.append(label)
    return predictions