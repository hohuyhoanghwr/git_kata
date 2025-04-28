import pandas as pd
import numpy as np
def load_data(path):
    df = pd.read_csv(path)
    df = df[df['sex'] == "male"]
    return df