import pandas as pd
import numpy as np
import requests as rq
import json

df = pd.read_csv('/home/dark/Transferências/train.csv')
formula = 0

# trato os NaN (Not A Number)
df = df.replace(np.nan, 0)


# pesos
# MT = 3, CN = 2, LC = 1.5, CH = 1, NOTA_REDACAO = 3

def nota_final(mt, cn, lc, ch, r):
    """

    :rtype: float
    """
    formula = ((mt * 3) + (cn * 2) + (lc * 1.5) + (ch * 1) + (r * 3)) / 10.5
    return formula


new_col = []
for index, row in df.iterrows():
    new_col.append(round(
        nota_final(row['NU_NOTA_MT'], row['NU_NOTA_CN'], row['NU_NOTA_LC'], row['NU_NOTA_CH'], row['NU_NOTA_REDACAO']),
        1))

# Insiro a nova coluna com as notas finais
df.insert(loc=0, column='NOTA_FINAL', value=new_col)

# Ordeno Dataframe pela nota
df = df.sort_values(by='NOTA_FINAL', ascending=False)

# Pego os 20 primeiros resultados
resultf = df.head(20)
resultf = resultf[['NU_INSCRICAO', 'NOTA_FINAL']]

# Header do Json - modelo Code:nation
resultJson = '{"token": "460c08daf59a7d4a88418a9ebb6bcfc52d30afae","email": "rpedrodasilva10@gmail.com","answer":'

out = resultf.to_json(orient='records')
out = resultJson + out + '}'
out = json.loads(out)

r = rq.post("https://api.codenation.com.br/v1/user/acceleration/data-science/challenge/enem-1/submit", json=out)
print(r.status_code)
print(r.content)
