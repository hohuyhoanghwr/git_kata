import pandas as pd
import numpy as np
def load_data(path):
    df = pd.read_csv(path)
    df = df[df['sex'] == "male"]
    return df

def clean_data(df):
    """
    comment1
    comment2
    comment3
    """
    df = df.dropna(axis=1)
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.lower()
    return df