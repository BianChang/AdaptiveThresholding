import numpy as np
from scipy.ndimage import median_filter, uniform_filter1d

def preprocess_data(data):
    # Apply smoothing to the data
    data = median_filter(data, size=3)
    data = uniform_filter1d(data, size=3)
    return data
