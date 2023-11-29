import pandas as pd
import os
from twilio.rest import Client 

account_sid = os.environ["AC00702ff6d7666265ba52248217da5e2f"]
auth_token = os.environ['32dcc18043bfc342fbfaa4b23e920303']
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if(tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc [tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc [tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
                     body=f"No mês {mes} a meta foi atingida. Vendedor:{vendedor} Valor:{vendas}",
                     from_='+14159693864',
                     to='5519996399383'
                 )
        print(message.sid)