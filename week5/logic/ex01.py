import pandas as pd
import requests as req
import matplotlib.pyplot as plt
import io


def statsbank_format(columns):
    url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?lang=en&delimiter=Semicolon"
    for columns in columns:
        url = url + "&"+columns+"=*"
    return url


def direct(columns):
    df = pd.read_csv(statsbank_format(columns), sep =';')
    return df


def divorced():
    '''
    What is the change in pct of divorced danes from 2008 to 2020?
    '''
    df = direct(['CIVILSTAND', 'TID'])
    
    df = df[df["CIVILSTAND"].str.match('Divorced')]
    fig, ax = plt.subplots()
    ax.plot(df['TID'], df['INDHOLD'])
    ax.legend()
    plt.show()
    

def never_married():
    '''
    Which of the biggest cities has the highest percentage of 'Never Married'?
    '''
    df = direct(['OMR%C3%85DE', 'CIVILSTAND'])
    df = df[df['CIVILSTAND'].str.match('Never married')]
    df = df.sort_values(by=['INDHOLD'])[-6:-1]

    df.plot.bar(x='OMRÅDE', y='INDHOLD')
    plt.show()


def marrital_status():
    '''
    Show a bar chart of changes in marrital status in Copenhagen from 2008 till now
    '''
    df = direct(['TID','OMR%C3%85DE', 'CIVILSTAND'])
    df = df[df['OMRÅDE'].str.match('Copenhagen')]
    df = df.drop(columns=['OMRÅDE'])
    df['TID'] = df['TID'].map(lambda x: x[:4])
    
    df1 = df[df['CIVILSTAND'].str.match('Married/separated')]
    df2 = df[df['CIVILSTAND'].str.match('Never married')]
    df3 = df[df['CIVILSTAND'].str.match('Widowed')]
    df4 = df[df['CIVILSTAND'].str.match('Divorced')]

    df['MARSEP'] = df1['INDHOLD']

    df = df.drop(columns=['CIVILSTAND'])
    df = df.drop(columns=['INDHOLD'])
    df = df.dropna()

    df = df.drop_duplicates(subset=['TID'])

    df = df.reset_index()
    df1 = df1.reset_index()
    df2 = df2.reset_index()
    df3 = df3.reset_index()
    df4 = df4.reset_index()

    df['NEVERMARRIED'] = df2['INDHOLD']
    df['WIDOWED'] = df3['INDHOLD']
    df['DIVORCED'] = df4['INDHOLD']

    df.plot(x='TID', y=['MARSEP', 'NEVERMARRIED', 'WIDOWED', 'DIVORCED'], kind="bar")
    plt.show()
    
def married_nevermarried():
    '''
    Show a bar chart of 'Married' and 'Never Married' for all ages in DK (Hint: 2 bars of different color)
    '''
    df = direct(['ALDER', 'CIVILSTAND'])
    df = df.drop(columns='TID')
    df = df[~df['ALDER'].str.match('Total')]
    df['ALDER'] = df['ALDER'].map(lambda x: x[:-6])

    df1 = df[df['CIVILSTAND'].str.match('Married/separated')]
    df2 = df[df['CIVILSTAND'].str.match('Never married')]

    df['MARRIED'] = df1['INDHOLD']
    df = df.drop(columns=['CIVILSTAND'])
    df = df.drop(columns=['INDHOLD'])
    df = df.dropna()

    df = df.drop_duplicates(subset=['ALDER'])
    df = df.reset_index()
    df2 = df2.reset_index()
    df['NEVER MARRIED'] = df2['INDHOLD']

    df.plot(x='ALDER', y=['MARRIED','NEVER MARRIED'], kind="bar", width=0.5)
    plt.show()


def create_csv(url):
    res = req.get(url, stream=True)
    with open("./resources/FOLK1A.csv", 'wb') as fileWriter:
        for line in res.iter_content():
            fileWriter.write(line)