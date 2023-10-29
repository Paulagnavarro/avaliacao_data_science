import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error

# Carregar os dados do arquivo CSV
data = pd.read_csv('C:/Users/Paula/Documents/Atividade_data_science/Vendas.csv', sep=';', encoding='iso-8859-1')

# Remover espaços em branco dos nomes das colunas
data.columns = data.columns.str.strip()

# Ajustar o formato do mês na coluna 'Mês' (remover espaços em branco)
data['Mês'] = data['Mês'].str.strip()

# Mapear os nomes dos meses para nomes em inglês
meses_em_portugues = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
meses_em_ingles = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

data['Mês'] = data['Mês'].replace(meses_em_portugues, meses_em_ingles)

# Converter a coluna 'Vendas (em unidades monetárias)' para tipo numérico
data['Vendas (em unidades monetárias)'] = data['Vendas (em unidades monetárias)'].str.replace(',', '.').astype(float)

# Criar uma coluna 'Data' combinando 'Ano' e 'Mês'
data['Data'] = pd.to_datetime(data['Ano'].astype(str) + '-' + data['Mês'] + '-01', format='%Y-%B-%d')

# Defina a coluna 'Data' como o índice do DataFrame
data.set_index('Data', inplace=True)

# suavização exponencial para a previsão
model = ExponentialSmoothing(data['Vendas (em unidades monetárias)'], seasonal='add', seasonal_periods=12)
model_fit = model.fit()

# Fazer a previsão para o próximo ano (12 meses à frente)
forecast = model_fit.forecast(steps=12)

# Calcular o erro médio absoluto (MAE) considerando apenas as últimas 12 amostras
mae = mean_absolute_error(data['Vendas (em unidades monetárias)'][-12:], forecast)

print(f'Erro Médio Absoluto (MAE): {mae:.2f}')

# Inicializar variáveis para o cálculo do MAPE
mape_sum = 0
n = 0

# Calcular o MAPE 
for i in range(12):
    real_value = data['Vendas (em unidades monetárias)'].iloc[-12 + i]
    forecast_value = forecast[i]
    if real_value != 0:
        mape_sum += (abs(real_value - forecast_value) / real_value) * 100
        n += 1

mape = mape_sum / n if n > 0 else 0

print(f'Erro Percentual Médio Absoluto (MAPE): {mape:.2f}%')

# resultados
plt.figure(figsize=(12, 6))
plt.plot(data['Vendas (em unidades monetárias)'], label='Vendas Observadas')
plt.plot(forecast, label='Previsão 2028')
plt.legend()
plt.xlabel('Data')
plt.ylabel('Vendas (em unidades monetárias)')
plt.title('Previsão de Vendas para 2028')
plt.show()

# Fazer a previsão para os próximos cinco anos (60 meses à frente)
forecast = model_fit.forecast(steps=60)

# resultados
plt.figure(figsize=(12, 6))
plt.plot(data['Vendas (em unidades monetárias)'], label='Vendas Observadas')
plt.plot(forecast, label='Previsão 2028-2032')
plt.legend()
plt.xlabel('Data')
plt.ylabel('Vendas (em unidades monetárias)')
plt.title('Previsão de Vendas para 2028-2032')
plt.show()


# Modelo de suavização exponencial


# Limitações:

# Tamanho do conjunto de dados: O desempenho de métodos de previsão, como a suavização exponencial, 
# muitas vezes depende do tamanho do conjunto de dados. Se você tiver um conjunto de dados muito pequeno, 
# a capacidade do modelo de fazer previsões precisas pode ser limitada.

# Assunções da suavização exponencial: A suavização exponencial assume que os dados seguem um padrão 
# exponencial de suavização e não levam em consideração tendências complexas, sazonalidades irregulares 
# ou valores atípicos. Essa é uma limitação importante, pois a realidade dos dados pode ser mais complexa.

# Métricas de erro: Embora o código calcule métricas de erro, como MAE e MAPE, é importante considerar 
# que essas métricas são apenas indicadores da qualidade da previsão. Elas não oferecem insights 
# sobre o motivo das discrepâncias entre as previsões e os valores reais.


# Sugestões para um Cenário Real:

# Conjunto de Dados Adequado: Para previsões mais precisas, é importante ter um conjunto de dados 
# históricos de vendas de tamanho suficiente. Quanto mais dados históricos você tiver, melhor o modelo
# poderá capturar padrões.

# Consideração de Fatores Externos: Se houver fatores externos que influenciam as vendas 
# (por exemplo, sazonalidades específicas da indústria), é importante incorporar esses fatores no modelo 
# de previsão para melhorar a precisão.

# Monitoramento Contínuo: Em um cenário real, o monitoramento contínuo das previsões é essencial. 
# À medida que novos dados se tornam disponíveis, o modelo deve ser atualizado e recalibrado, se necessário.

# Interpretação dos Resultados: Além de calcular métricas de erro, é importante entender por que o modelo 
# fez certas previsões. A interpretação dos resultados é fundamental para a tomada de decisões.


# Suposições Subjacentes:

# Estacionariedade: O modelo de suavização exponencial assume que os dados são estacionários, ou seja, 
# que não possuem tendências significativas ou sazonalidades que mudam ao longo do tempo. 

# Continuidade do Padrão: O modelo de suavização exponencial assume que o padrão observado no passado 
# continuará no futuro. Se houver mudanças drásticas nas condições de mercado, concorrência, política, ou 
# outros fatores que afetem as vendas, o modelo pode não capturar essas mudanças.

# Independência dos Erros: O modelo de suavização exponencial assume que os erros de previsão são 
# independentes e normalmente distribuídos. Isso significa que os erros de previsão devem ser aleatórios 
# e não correlacionados. Se houver autocorrelação nos erros, isso pode indicar que o modelo não está 
# capturando todos os padrões subjacentes.

# Influência de Fatores Externos: O modelo de suavização exponencial não leva em consideração fatores 
# externos que podem afetar as vendas, como mudanças econômicas, lançamento de novos produtos, 
# eventos sazonais, entre outros.

# Monitoramento Contínuo: Previsões de longo prazo devem ser monitoradas continuamente e recalibradas 
# à medida que novos dados se tornam disponíveis. O cenário real pode evoluir de maneira imprevisível ao 
# longo dos cinco anos.