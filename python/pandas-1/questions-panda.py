import numpy as np
import pandas as pd
import mysqldb


def q1():
    df = pd.read_csv('/home/dark/codenation/pandas-1/data.csv')['nationality']
    df = df.unique()
    return len(df)

def q2():
    df = pd.read_csv('/home/dark/codenation/pandas-1/data.csv')['club']
    df = df.unique()
    return len(df)


def q3():
    df = pd.read_csv('/home/dark/codenation/pandas-1/data.csv')['full_name']
    return df.head(10)

def q4():
    df = pd.read_csv('/home/dark/codenation/pandas-1/data.csv')
    col = ['full_name', 'eur_wage']
    df = df[col].head(10)
    return df


def q5():
    df = pd.read_csv('/home/dark/codenation/pandas-1/data.csv')
    col = ['full_name', 'age']
    df = df[col].sort_values(by='age', ascending=False).head(10)
    df = df['full_name']
    return df

def q6():
    df = pd.read_csv('/home/dark/codenation/pandas-1/data.csv')
    col = ['age']
    df = df[col]
    df = df.groupby('age').count()  
    print(df)
    #return df.sum()
    #print(df)
#print(q1())
#print(q2())
#print(q3())
#print(q4())
#print(q5())
print(q6())