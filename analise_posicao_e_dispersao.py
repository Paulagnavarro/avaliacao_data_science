import pandas as pd

# Carregar os dados do arquivo CSV
data = pd.read_csv('C:/Users/Paula/Documents/Atividade_data_science/Vendas.csv', sep=';', encoding='iso-8859-1')

# Remover espaços em branco dos nomes das colunas
data.columns = data.columns.str.strip()

# Converter virgulas em pontos
data['Vendas (em unidades monetárias)'] = data['Vendas (em unidades monetárias)'].str.replace(',', '.').astype(float)

# Calcular a média das vendas
media_vendas = data['Vendas (em unidades monetárias)'].mean()

# Agrupar os dados por ano
grupo_por_ano = data.groupby('Ano')

# Calcular a mediana para cada ano
mediana_por_ano = grupo_por_ano['Vendas (em unidades monetárias)'].median()

# Agrupar os dados por mês e calcular a variância e o desvio padrão
vendas_por_mes = data.groupby('Mês')['Vendas (em unidades monetárias)']
variancia_por_mes = vendas_por_mes.var()
desvio_padrao_por_mes = vendas_por_mes.std()

# Encontrar o mês com a maior venda
linha_maior_venda = data[data['Vendas (em unidades monetárias)'] == data['Vendas (em unidades monetárias)'].max()]

# Encontrar o mês com a menor venda
linha_menor_venda = data[data['Vendas (em unidades monetárias)'] == data['Vendas (em unidades monetárias)'].min()]

# Identificar meses atípicos (aqueles que estão muito acima ou abaixo da média)
desvio_padrao_total = data['Vendas (em unidades monetárias)'].std()
limite_superior = media_vendas + 2 * desvio_padrao_total
limite_inferior = media_vendas - 2 * desvio_padrao_total

meses_atipicos = data[(data['Vendas (em unidades monetárias)'] > limite_superior) | (data['Vendas (em unidades monetárias)'] < limite_inferior)]['Mês']

# Imprimir os resultados
print("Média das vendas:", media_vendas)
print("Mediana das vendas por ano:")
print(mediana_por_ano)
print("Variância das vendas por mês:")
print(variancia_por_mes)
print("\nDesvio padrão das vendas por mês:")
print(desvio_padrao_por_mes)
print("Mês com a maior venda:", linha_maior_venda['Mês'].values[0], "do ano", linha_maior_venda['Ano'].values[0])
print("Mês com a menor venda:", linha_menor_venda['Mês'].values[0], "do ano", linha_menor_venda['Ano'].values[0])
print("Média das vendas de todos os meses:", media_vendas)
print("Meses atípicos:", meses_atipicos)


# A média é considerada uma referência central, pois está localizada no centro da distribuição das vendas. 
# Ela é uma estimativa do ponto central em torno do qual as vendas variam.

# A mediana é um valor que divide o conjunto de dados em duas partes iguais, onde metade dos valores estão 
# acima dela e metade dos valores estão abaixo dela. Diferentemente da média, a mediana não é afetada por 
# valores extremos nos dados, o que a torna uma medida de tendência central mais robusta em 
# relação a valores atípicos.

# Variância da vendas por mês:
# As vendas têm a menor variância em novembro e julho, com 0.09, indicando que esses meses têm
# menos dispersão nas vendas.
# Por outro lado, março tem a maior variância, com 0.30, indicando que há uma maior variabilidade nas 
# vendas em março.

# Desvio Padrão das vendas:
# Março tem o maior desvio padrão, com aproximadamente 0.551, o que significa que as vendas nesse mês 
# variam consideravelmente em relação à média.
# Novembro e julho têm o menor desvio padrão, com aproximadamente 0.300, indicando que as vendas 
# nesses meses são mais consistentes em relação à média.