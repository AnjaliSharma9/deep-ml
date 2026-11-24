
import numpy as np

def gini_impurity(y):
    """
    Calculate Gini Impurity for a list of class labels.

    :param y: List of class labels
    :return: Gini Impurity rounded to three decimal places
    """
    y = np.asarray(y)
    n = np.size(y)

    _, counts = np.unique(y, return_counts=True)
    p = counts / n
    val = 1 - np.sum(p**2)

    return round(val,3)
    pass

    #y == 0 gives an array of True and False, one per label, where True means that label is 0. np.sum adds those up, and because True counts as 1 and False as 0, the total is the number of zeros.