import pandas as pd

# Carregar os dados do arquivo CSV
data = pd.read_csv('C:/Users/Paula/Documents/Atividade_data_science/Vendas.csv', sep=';', encoding='iso-8859-1')

# Remover espaços em branco dos nomes das colunas
data.columns = data.columns.str.strip()

# Converter virgulas em pontos
data['Vendas (em unidades monetárias)'] = data['Vendas (em unidades monetárias)'].str.replace(',', '.').astype(float)

# Calcular os quartis
quartis = data['Vendas (em unidades monetárias)'].quantile([0.25, 0.5, 0.75])

# Calcular o intervalo interquartil (IQR)
IQR = quartis[0.75] - quartis[0.25]

# Exibir os valores dos quartis
print("Primeiro Quartil (Q1):", quartis[0.25])
print("Segundo Quartil (Mediana - Q2):", quartis[0.5])
print("Terceiro Quartil (Q3):", quartis[0.75])
# Exibir o intervalo interquartil
print("Intervalo Interquartil (IQR):", IQR)


# O IQR é uma medida estatística que representa a variação da metade central dos dados, excluindo 
# valores extremos. Ele é útil para identificar a dispersão dos dados em torno da mediana, proporcionando 
# uma compreensão da variabilidade da metade central da distribuição.

# Quanto maior o IQR, maior a dispersão na metade central dos dados, indicando que os valores estão mais 
# espalhados. Um IQR menor indica que os valores estão mais próximos da mediana e têm menos dispersão 
# na metade central.