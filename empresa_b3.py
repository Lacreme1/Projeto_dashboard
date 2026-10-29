import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Carregando os dados
df = pd.read_excel('ABEV3_evolucao.xlsx')
st.write(df)

# Estatísticas da coluna 'valor'
st.write("Máximo:", df['valor'].max())
st.write("Mínimo:", df['valor'].min())
st.write("Média:", df['valor'].mean())
st.write("Desvio Padrão:", df['valor'].std())

# Filtrando linhas através do valor do trimestre ('20262T')
linhas_trimestre = (df['trimestre'] == '20262T')
colunas_filtro = ['conta', 'valor']
st.write("Dados do trimestre 20262T:", df.loc[linhas_trimestre, colunas_filtro])

# Média do lucro total
linhas_lucro = (df['conta'] == 'lucro')
media_lucro = df.loc[linhas_lucro, 'valor'].mean()
st.write("Média do Lucro:", media_lucro)

# Gráfico do lucro por trimestre
fig, ax = plt.subplots(figsize=(10, 5))
dados_grafico = df[df['conta'] == 'lucro']

sns.lineplot(data=dados_grafico, x='trimestre', y='valor', ax=ax)
ax.set_title('Gráfico do Lucro')
plt.xticks(rotation=45)

# Exibindo o gráfico no Streamlit
st.pyplot(fig)
