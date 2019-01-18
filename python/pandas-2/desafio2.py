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


#desafio 2

#Arquivo de treino da machine
df_train = pd.read_csv('/home/dark/Transferências/train.csv')
#df_train = df_train.replace(r'\s+',np.nan,regex=True)
df_train = df_train.fillna(0)

#Arquivo de teste da machine
df_test = pd.read_csv('/home/dark/Transferências/test2.csv')
df_test = df_test.fillna(0)

#df_test = df_test['IN_DISLEXIA']

#df_train = df_train.sort_values(by='IN_DISLEXIA',ascending=False)

#Colunas

#cols = ['IN_DISCALCULIA', 'IN_DISLEXIA', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_REDACAO', 'NU_NOTA_LC','TP_ESCOLA'\
#,'TP_ENSINO','TP_PRESENCA_CN','TP_PRESENCA_LC','TP_PRESENCA_CH','TP_LINGUA', 'TP_STATUS_REDACAO']

#cols = ['CO_UF_RESIDENCIA',	'NU_IDADE',	'TP_COR_RACA',	'TP_NACIONALIDADE',\
#        'TP_ST_CONCLUSAO', 'TP_ANO_CONCLUIU', 'TP_ESCOLA','TP_ENSINO',	'IN_TREINEIRO',	'TP_DEPENDENCIA_ADM_ESC',\
#        'IN_DISLEXIA',	'IN_DISCALCULIA',	'IN_SABATISTA',\
#        'IN_GESTANTE',	'IN_IDOSO',	'TP_PRESENCA_CN',	'TP_PRESENCA_CH',	'TP_PRESENCA_LC',\
#        'NU_NOTA_CN',	'NU_NOTA_CH',	'NU_NOTA_LC',	'TP_LINGUA', 'TP_STATUS_REDACAO',	'NU_NOTA_COMP1',\
#        'NU_NOTA_COMP2',	'NU_NOTA_COMP3',	'NU_NOTA_COMP4', 'NU_NOTA_COMP5',	'NU_NOTA_REDACAO']


cols = ['NU_NOTA_LC','NU_NOTA_CN','TP_PRESENCA_LC','NU_NOTA_CH','NU_NOTA_COMP1',\
        'NU_NOTA_REDACAO','NU_NOTA_COMP4','NU_NOTA_COMP2']
# TP_ANO_CONCLUIU’, TP_ESCOLA, IN_TREINEIRO, IN_DISLEXIA, IN_DISCALCULIA, IN_IDOSO, NU_NOTA_CN	,
# TP_ST_CONCLUSAO, TP_ENSINO,


#0.8986361464731297

#PLOT para verificar a relação entre as variaveis
#sns.pairplot(df_train,x_vars=['TP_ST_CONCLUSAO'],y_vars='NU_NOTA_MT', kind='reg')

#0.8895383068249108
#889533056105035
#8902428344049242
#8938085886151234
#0.8973562165055402
#0.8974815774832898
#0.8980869350987513
#Valores que tem relação com o resultado



#Skewneess/Kurtosis
print("Skewness: %f" % df_train['NU_NOTA_MT'].skew())
print("Kurtosis: %f" % df_train['NU_NOTA_MT'].kurt())

X = df_train.loc[:, cols]
df_preview = df_test.loc[:, cols]
#Coluna a ser prevista
y = df_train['NU_NOTA_MT']

#Learn
linreg.fit(X, y)


#corrmat = df_train.corr()
#f, ax = plt.subplots(figsize=(12, 9))
#sns.heatmap(corrmat, vmax=.8, square=True);


#Valores previstos
pre = linreg.predict(df_preview)

#Percentual de acerto
print(linreg.score(X,y))

#print(linreg.intercept_)

#print(linreg.coef_)
#print(zip(cols, linreg.coef_))

#y_pred = linreg.predict(X)

#print(np.sqrt(mt.mean_squared_error(y,y_pred))/100)
plt.show()

#DataFrame de resposta
dfres = pd.DataFrame()
dfres.insert(loc=0,column='NU_INSCRICAO',value=df_test['NU_INSCRICAO'])
dfres.insert(loc=1,column='NU_NOTA_MT',value=pre,allow_duplicates=True)

#post
resultf = dfres[['NU_INSCRICAO','NU_NOTA_MT']]
#print(resultf)
# Header do Json - modelo Code:nation
resultJson = '{"token": "460c08daf59a7d4a88418a9ebb6bcfc52d30afae","email": "rpedrodasilva10@gmail.com","answer":'

out = resultf.to_json(orient='records')
out = resultJson + out + '}'
out = json.loads(out)

#r = rq.post("https://api.codenation.com.br/v1/user/acceleration/data-science/challenge/enem-2/submit", json=out)
#print(r.status_code)
#print(r.content)

#NOTAS CODENATION
#89.25598884349057