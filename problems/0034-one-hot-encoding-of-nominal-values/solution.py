import numpy as np

def to_categorical(x, n_col=None):
    if n_col == None:
        n_col = np.max(x)+1
    return np.eye(n_col)[x]

    #np.eye(n_col) is a lookup table where row k is the one-hot vector for category k.

    pass