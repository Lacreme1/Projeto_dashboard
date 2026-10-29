import pandas as pd

df = pd.read_excel('ABEV3_evolucao.xlsx')
print(df)
# selecionando a coluna 'valor' e aplicando funções estatísticas
df['valor'].max()
df['valor'].min()
df['valor'].mean()
df['valor'].std()
# selecionar linhas
df[0:1]
# selecionando linhas e colunas
colunas = ['conta','valor']
df[23:24][colunas]
# filtrar linhas atraves valor
df['trimestre'] == '20262T'
colunas = ['conta','valor']
df[linhas][colunas]
# Lucros total
linhas = df ['conta'] == 'lucro'
colunas = ['valor']
df[linhas][colunas].mean()
# Importação para gráficos
import seaborn as sns
import matplotlib.pyplot as plt
# grafico
import seaborn as sns
dados= df[linhas][colunas]
sns.lineplot(dados)
# Gráfico do lucro
linhas = df['conta'] == 'lucro'
colunas = ['trimestre', 'valor']
dados = df[linhas][colunas]
sns.lineplot(dados,x= 'trimestre', y='valor')
plt.title('grafico do lucro')
plt.xticks(rotatiom=45)