import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    mean = data.mean(axis = 0)
    std = data.std(axis = 0, ddof = 0 )
    standardized_data = (data - mean)/std
    
    min = data.min(axis = 0)
    max = data.max(axis = 0)
    normalized_data = (data - min)/(max - min)
    return standardized_data, normalized_data