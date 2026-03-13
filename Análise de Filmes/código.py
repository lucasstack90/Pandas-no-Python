import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados do arquivo
df_movies = pd.read_csv('movies.csv')

# 2. Separar os gêneros (estão divididos por '|') e contar as ocorrências
# Isso cria uma lista individual para cada gênero mencionado
generos_separados = df_movies['genres'].str.split('|').explode()
contagem_generos = generos_separados.value_counts()

# 3. Filtrar apenas os que você pediu (e mais alguns populares para comparar)
alvos = ['Drama', 'Crime', 'Comedy', 'Action', 'Adventure', 'Animation']
dados_filtrados = contagem_generos.loc[contagem_generos.index.isin(alvos)]

# 4. Criar o gráfico de barras
plt.figure(figsize=(10, 6))
dados_filtrados.plot(kind='bar', color='royalblue')

# 5. Customização
plt.title('Quantidade de Filmes por Gênero', fontsize=14)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Total de Filmes', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()