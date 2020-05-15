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

1. X = Time, Y = Employees working in Sea Transport export division. Bar

2. find post *, all, 2018, total. multibar
3. find Research and development services, tid *, VIRKSTRRDA *, multibar
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

    print(df)

    df.plot.bar(x='TID', y='INDHOLD')
    plt.show()

def all2018():
    df = direct(['POST','INDUD','VIRKSTRRDA','TID'])

    df = df[df['VIRKSTRRDA'].str.match('Total')]
    df = df[df['TID']==2018]
    
    df['TID'] = pd.to_numeric(df['TID'])
    df['INDHOLD'] = pd.to_numeric(df['INDHOLD'],errors='coerce')
    df['EXPORT'] = df[df['INDUD'].str.match('Exports')]['INDHOLD']
    df1 = df[df['INDUD'].str.match('Imports')]

    df = df.drop(columns='VIRKSTRRDA')
    df = df.drop(columns='TID')
    df = df.dropna()
    df = df.reset_index(drop=True)
    df1 = df1.reset_index(drop=True)

    df['IMPORT'] = df1['INDHOLD']

    df.plot.bar(x='POST', y=['EXPORT','IMPORT'])
    plt.show()



def research():
    df = direct(['POST','INDUD','VIRKSTRRDA','TID'])

    df = df[df['POST'].str.match("Research and development services")]
    df = df[~df['VIRKSTRRDA'].str.match("Total")]
    df = df[df['INDUD'].str.match('Exports')]
    df['INDHOLD'] = pd.to_numeric(df['INDHOLD'])
    print(df)
    df['LOW'] = df[df['VIRKSTRRDA'].str.match("From 0 to 49 employees")]['INDHOLD']
    df['MEDIUM'] = df[df['VIRKSTRRDA'].str.match("From 50 to 249 employees")]['INDHOLD']
    df['HIGH'] = df[df['VIRKSTRRDA'].str.match("250 employees or more")]['INDHOLD']
    df['UNKNOWN'] = df[df['VIRKSTRRDA'].str.match("Unknown")]['INDHOLD']
    df = df.drop(columns='INDHOLD')
    df = df.groupby(['TID', 'VIRKSTRRDA']).max()
    df = df.reset_index()
   # print(df)
    #df.plot.bar(x='TID', y=['LOW','MEDIUM','HIGH','UNKNOWN'], stacked=True)
    #plt.show()

    

def finance():
    raise NotImplemented()

def construction():
    raise NotImplemented()

