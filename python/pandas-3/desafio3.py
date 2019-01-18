import pandas as pd
import requests as rq
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics as mt
import seaborn as sns#;  sns.set(style="ticks",color_codes=True)

linreg = LinearRegression()


#desafio 3

#Arquivo de treino da machine
df_train = pd.read_csv('/home/dark/Transferências/train.csv')
#df_train = df_train.replace(r'\s+',np.nan,regex=True)
df_train = df_train.fillna(0)

#Arquivo de teste da machine
df_test = pd.read_csv('/home/dark/Transferências/test3.csv')
df_test = df_test.fillna(0)


UPDATE TABELA
SET CAMPO1 = 'VALOR 1', CAMPO2 = 'VALOR2', CAMPON = 'VALORN'
