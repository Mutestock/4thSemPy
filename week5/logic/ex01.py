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

    df['TID'] = df['TID'].map(lambda x: x[:4])
    
    df1 = df[df['CIVILSTAND'].str.match('Married/separated')]
    df2 = df[df['CIVILSTAND'].str.match('Never married')]
    df3 = df[df['CIVILSTAND'].str.match('Widowed')]
    df4 = df[df['CIVILSTAND'].str.match('Divorced')]

    df['MARSEP'] = df1['INDHOLD']
    df['NEVERMARRIED'] = df2['INDHOLD']
    df['WIDOWED'] = df3['INDHOLD']
    df['DIVORCED'] = df4['INDHOLD']

    df.plot(x='TID', y=['MARSEP', 'NEVERMARRIED', 'WIDOWED', 'DIVORCED'], kind="bar")
    plt.show()
    
def married_nevermarried():
    '''
    Show a bar chart of 'Married' and 'Never Married' for all ages in DK (Hint: 2 bars of different color)

    Note: why bar? You need to maximize the window to watch the "correct" representation of the data.
    '''
    df = direct(['ALDER', 'CIVILSTAND'])
    df = df[~df['ALDER'].str.match('Total')]

    df['MARRIED'] = df[df['CIVILSTAND'].str.match('Married/separated')]['INDHOLD']
    df['NEVERMARRIED'] = df[df['CIVILSTAND'].str.match('Never married')]['INDHOLD']
   
    df.plot(x='ALDER', y=['MARRIED','NEVERMARRIED'], kind="bar", width=0.5)
    plt.show()


def create_csv(url):
    res = req.get(url, stream=True)
    with open("./resources/FOLK1A.csv", 'wb') as fileWriter:
        for line in res.iter_content():
            fileWriter.write(line)