import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import estimate_bandwidth, MeanShift
import matplotlib.pyplot as plt

def load_csv():
    '''
    1. load 'iris_data.csv into a dataframe'
    '''
    df = pd.read_csv('resources/iris_data.csv')
    return df

def unique_labels():
    '''
    2. get unique labels(Species column)

    ????
    '''
    df = load_csv()
    arr = np.unique(df['Species'].values)
    return df, arr

def encode():
    df,_ = unique_labels()
    label_enc = preprocessing.LabelEncoder()
    df['Species'] = label_enc.fit_transform(df['Species'].astype(str))
    return df

def scatter01():
    """
    3. plot with a scatter plot each iris flower sample colored by label(3 different colors)
    """    
    df = encode()
    fig, axes = plt.subplots(nrows=2)

    df.plot.scatter(ax=axes[0], x='Petal length', y='Petal width', c='Species', colormap='viridis')
    df.plot.scatter(ax=axes[1],x='Sepal length', y='Sepal width', c='Species', colormap='viridis')

    plt.show()

def cluster():
    """
    4. use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate bandwidth and then get the clusters 
    (HINT: estimate_bandwidth() takes an argument: quantile set it to 0.2 for best result
    """    
    df = encode().replace(',','.',regex=True)
    bandwidth = estimate_bandwidth(df,quantile=0.2)
    analyzer = MeanShift(bandwidth=bandwidth)
    analyzer.fit(df)

    labels = analyzer.labels_
    centers = analyzer.cluster_centers_

    return bandwidth, labels, centers

def cluster_print():
    """
    5. print labels, cluster centers and number of clusters (as returned from the MeanShift function)
    """    

    bandwidth, labels, centers = cluster()
    unique = np.unique(labels)

    print('\n\n#########\n')
    print(f"Bandwidth: {bandwidth}\n")
    print(f'Labels:\n {labels}\n')
    print(f'Unique labels: {unique}\n')
    print(f'Centers: {centers}\n')
    print(f'Cluster count: {len(centers)}\n')
    print('########\n')

def scatter02():
    