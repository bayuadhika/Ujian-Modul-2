import pandas as pd
import numpy as np
import seaborn as sns

def IndiaClean():
    df = pd.read_csv('clean.csv')
    return df.head(20)
