# -*- coding: utf-8 -*-
"""DadosCB.ipynb

"""

pip install python-bcb

import bcb

from bcb import Expectativas
import pandas as pd
# Obtém as informações da API de expectativas

expec = Expectativas()

# Busca o endpoint

expec.describe('ExpectativasMercadoAnuais')
expec.describe('ExpectativasMercadoTop5Anuais')

# Importa o endpoint
ep = expec.get_endpoint(('ExpectativasMercadoAnuais'))

# Aqui limitamos a data de coleta para retirar dados apartir do dia 01/01/2021 para reduzir o tempo de consulta
# Limitamos a coleta aos principais dados do Relatório Focus de mercado

ep.query().filter((ep.Indicador == 'IPCA'),(ep.Data >= '2021-01-01')).collect()
ep.query().filter((ep.Indicador == 'Selic'),(ep.Data >= '2021-01-01')).collect()
ep.query().filter((ep.Indicador == 'Câmbio'),(ep.Data >= '2021-01-01')).collect()
ep.query().filter((ep.Indicador == 'IGP-M'),(ep.Data >= '2021-01-01')).collect()
ep.query().filter((ep.Indicador == 'PIB Total'),(ep.Data >= '2021-01-01')).collect()

# prompt: transforma a tabela acima em um arquivo xlsx
# Cria um DataFrame a partir da tabela
#Selecionamos a data apartir do dia 01/01/2021 para agilizar a coleta, mas pode ser alterado de acordo com a vontade do usuário
Tabela_IPCA = pd.DataFrame(ep.query().filter((ep.Indicador == 'IPCA'),(ep.Data >= '2021-01-01')).collect())
Tabela_Selic = pd.DataFrame(ep.query().filter((ep.Indicador == 'Selic'),(ep.Data >= '2021-01-01')).collect())
Tabela_Câmbio = pd.DataFrame(ep.query().filter((ep.Indicador == 'Câmbio'),(ep.Data >= '2021-01-01')).collect())
Tabela_PIB = pd.DataFrame(ep.query().filter((ep.Indicador == 'PIB Total'),(ep.Data >= '2021-01-01')).collect())
Tabela_IGPM = pd.DataFrame(ep.query().filter((ep.Indicador == 'IGP-M'),(ep.Data >= '2021-01-01')).collect())

#concatena as tabelas criadas acima em uma única
df = pd.concat([Tabela_IPCA, Tabela_Selic, Tabela_Câmbio, Tabela_PIB, Tabela_IGPM])

# Salva o DataFrame como um arquivo Excel (utilizando o google colab)
df.to_excel('expectativas_ipca.xlsx', sheet_name='Sheet1')

from google.colab import files
files.download("expectativas_ipca.xlsx")
