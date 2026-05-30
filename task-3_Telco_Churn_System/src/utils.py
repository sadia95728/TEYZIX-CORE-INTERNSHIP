import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    return pd.read_csv(path)

def basic_info(df):
    print("Shape:", df.shape)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nData types:\n", df.dtypes)