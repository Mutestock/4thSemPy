import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Choose any of the other tables in 'databanken' to find interesting data

table id: DKSTEC1

Possible columns:
POST
Tid
INDUD (required)
VIRKSTRRDA (required)

'''

def dkstec1_format(columns):
    '''
    Collect the data
    '''
    url = "https://api.statbank.dk/v1/data/DKSTEC1/CSV?lang=en&delimiter=Semicolon"
    for columns in columns:
        url = url + "&"+columns+"=*"    
    return url


def direct(columns):
    df = pd.read_csv(dkstec1_format(columns), sep =';')
    return df


'''
Questions:

1. find Sea transport, export, year, employee count. Bar
2. find post *, export, 2018, total. Bar
3. find and sort Research and development, tid *, VIRKSTRRDA *, multibar
4. financial services, 2018, exports, virkstrrda*, pie
5. construction, 2014, *, total, pie

'''

def sea_employee_count():
    df = direct(['POST','INDUD','VIRKSTRRDA','TID'])
    
    df = df[df['POST'].str.match('Sea transport')]
    df = df[df['INDUD'].str.match('Exports')]
    df = df[df['VIRKSTRRDA'].str.match('Total')]

    df['TID'] = pd.to_numeric(df['TID'])
    df['INDHOLD'] = pd.to_numeric(df['INDHOLD'])

    df.plot.bar(x='TID', y='INDHOLD')
    plt.show()

def all2018():
    df = direct(['INDUD','VIRKSTRRDA','TID'])

    df = df[df['VIRKSTRRDA'].str.match('Total')]
    df['ALL'] = [pd.to_numeric(df['INDUD'].str.match('Exports'))+pd.to_numeric(df['INDUD'].str.match("Imports"))]
    df.drop(columns=['INDUD'])

def research():
    raise NotImplemented()

def finance():
    raise NotImplemented()

def construction():
    raise NotImplemented()

