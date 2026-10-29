import pandas as pd

pd.read_csv('alunos_desempenho.csv')

df = pd.read_csv('alunos_desempenho.csv')
df.head()
df.colunas
colunas=['aluno','curso','periodo']
df[colunas]

pd.read_excel('alunos_localidade_carro_merge.xlsx')