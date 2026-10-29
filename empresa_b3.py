import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados
df = pd.read_excel('ABEV3_evolucao.xlsx')
print(df)

# Selecionando a coluna 'valor' e aplicando funções estatísticas
print(df['valor'].max())
print(df['valor'].min())
print(df['valor'].mean())
print(df['valor'].std())

# Selecionando linhas específicas (exemplo: primeira linha)
print(df[0:1])

# Selecionando linhas e colunas específicas
colunas = ['conta', 'valor']
print(df.loc[23:24, colunas])

# Filtrando linhas através do valor do trimestre
linhas_trimestre = df['trimestre'] == '20262T'
colunas_filtro = ['conta', 'valor']
print(df.loc[linhas_trimestre, colunas_filtro])

# Média do lucro total
linhas_lucro = df['conta'] == 'lucro'
coluna_valor = ['valor']
print(df.loc[linhas_lucro, coluna_valor].mean())

# Gráfico do lucro por trimestre
fig, ax = plt.subplots(figsize=(10, 5))
dados_grafico = df[df['conta'] == 'lucro']

sns.lineplot(data=dados_grafico, x='trimestre', y='valor', ax=ax)
ax.set_title('Gráfico do Lucro')
plt.xticks(rotation=45)

# Se estiver usando Streamlit para exibir gráficos, use st.pyplot(fig)
import streamlit as st
st.pyplot(fig)
