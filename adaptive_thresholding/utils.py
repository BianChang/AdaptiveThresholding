import pandas as pd

def load_data(filepath):
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith('.txt'):
        return pd.read_csv(filepath, sep='\t')
    else:
        raise ValueError("Unsupported file format. Only .csv and .txt are supported.")

def save_data(dataframe, filepath):
    dataframe.to_csv(filepath, index=False)
