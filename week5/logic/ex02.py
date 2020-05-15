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

1. X = Time, Y = Services working in Sea Transport export division. Bar
2. X = Post, Y = services working in imports and exports in year 2018. Multibar
3. X = Time, Y = Research and development services exports division split up in VIRKSTRRDA:
    250 employees or more (HIGH)
    From 50 to 249 employees (MID)
    From 0 to 49 employees (LOW)
    Unknown (UNKNOWN)
 multibar
4. Pie diagram of financial services, 2018, exports, VIRKSTRRDA:
    250 employees or more (HIGH)
    From 50 to 249 employees (MID)
    From 0 to 49 employees (LOW)
    Unknown (UNKNOWN)

5. construction, 2014, *, total, pie

'''

def sea_employee_count():
    """
     X = Time, Y = Employees working in Sea Transport export division. Bar
    """    
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
    """X = Post, Y = Employees working in imports and exports in year 2018. Multibar
    """    
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
    """
    X = Time, Y = Research and development services exports division split up in:
        250 employees or more (HIGH)
        From 50 to 249 employees (MID)
        From 0 to 49 employees (LOW)
        Unknown (UNKNOWN)
    multibar
    """    
    df = direct(['POST','INDUD','VIRKSTRRDA','TID'])

    df = df[df['POST'].str.match("Research and development services")]
    df = df[~df['VIRKSTRRDA'].str.match("Total")]
    df = df[df['INDUD'].str.match('Exports')]
    df['INDHOLD'] = pd.to_numeric(df['INDHOLD'])
    
    df['LOW'] = df[df['VIRKSTRRDA'].str.match("From 0 to 49 employees")]['INDHOLD']

    df1 = df[df['VIRKSTRRDA'].str.match("From 50 to 249 employees")]
    df2 = df[df['VIRKSTRRDA'].str.match("250 employees or more")]
    df3 = df[df['VIRKSTRRDA'].str.match("Unknown")]

    df = df.drop(columns=['INDHOLD','POST', 'VIRKSTRRDA'])
    df = df.dropna()

    df = df.reset_index()
    df1 = df1.reset_index()
    df2 = df2.reset_index()
    df3 = df3.reset_index()

    df['MID'] = df1['INDHOLD']
    df['HIGH'] = df2['INDHOLD']
    df['UNKNOWN'] = df3['INDHOLD']
    
    df.plot.bar(x='TID', y=['LOW','MID','HIGH','UNKNOWN'], stacked=True)
    plt.show()

def finance():
    """
    Pie diagram of financial services, 2018, exports, VIRKSTRRDA:
        250 employees or more (HIGH)
        From 50 to 249 employees (MID)
        From 0 to 49 employees (LOW)
        Unknown (UNKNOWN)
    """    
    df = direct(['POST','INDUD','VIRKSTRRDA','TID'])
    df = df[df['POST'].str.match('FINANCIAL SERVICES')]
    df = df[df['TID'] == 2014]
    df = df[df['INDUD'].str.match('Exports')]

    df = df.drop(columns=['POST','TID','INDUD'])
    df = df[~df['VIRKSTRRDA'].str.match("Total")]
    df['INDHOLD'] = pd.to_numeric(df['INDHOLD'])
    df = df.reset_index()
    
    df.plot.pie(y='INDHOLD', figsize=(5,5), labels=df['VIRKSTRRDA'])
    plt.show()


def construction():
    raise NotImplemented()

