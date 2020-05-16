import pandas as pd
import numpy as np

def load_csv():
    '''
    load 'iris_data.csv into a dataframe'
    '''
    df = pd.read_csv('resources/iris_data.csv')
    return df

def unique_labels():
    '''
    get unique labels(Species column)
    '''
    df = load_csv()
    arr = np.unique(df['Species'].values)
    return df, arr

def scatter01():
    df, arr = unique_labels()
