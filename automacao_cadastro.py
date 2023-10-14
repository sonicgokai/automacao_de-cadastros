import pandas as pd
import bot_cadastro as bot

# Lendo o aqrquivo Excel dos cadastros dos clientes 
df = pd.read_excel('cadastro_clientes.xlsx')
bot.cadastro_web(df)