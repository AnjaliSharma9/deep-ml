import numpy as np

def rmse(y_true, y_pred):
    if np.shape(y_true) != np.shape(y_pred):
        raise ValueError("y_true and y_pred must have the same shape")
    if np.size(y_true) == 0:
        raise ValueError("arrays must not be empty")

    n = np.size(y_true)
    residual = y_true - y_pred
    rmse_res = np.sqrt(np.sum(residual**2)/n)

    return round(float(rmse_res), 3)