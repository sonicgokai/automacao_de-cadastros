from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def cadastro_web(dataframe):
    #Realizando login no sistema
        browser = webdriver.Chrome()      
        browser.maximize_window()
        browser.get('http://automacao.empowerdata.com.br')
        email = browser.find_element(By.XPATH, '//*[@id="email"]')
        email.send_keys('aluno@empowerdata.com.br')
        sleep(1)
    try:
        login = browser.find_element(By.XPATH, '//*[@id="password"]')
        login.send_keys('empowerpython')
        sleep(1)
        botao_entrar = browser.find_element(By.XPATH, '//*[@id="submit"]')
        botao_entrar.click()
        sleep(3)
    except:
        print('Login/senha invalido')
        
        
    
    # Iterando sobre o DataFrame
    for _, linha in dataframe.iterrows():
        nome_cliente = browser.find_element(By.XPATH, '//*[@id="nome"]')
        nome_cliente.send_keys(linha['Nome'])
        sleep(1)
        email_cliente = browser.find_element(By.XPATH, '//*[@id="email"]')
        email_cliente.send_keys(linha['E-mail'])
        sleep(1)
        telefone_cliente = browser.find_element(By.XPATH, '//*[@id="telefone"]')
        telefone_cliente.send_keys(linha['Telefone'])
        sleep(1)
        cidade_cliente = browser.find_element(By.XPATH, '//*[@id="cidade"]')
        cidade_cliente.send_keys(linha['Cidade'])
        sleep(1)
        estado_cliente = browser.find_element(By.XPATH, '//*[@id="estado"]')
        estado_cliente.send_keys(linha['Estado'])
        sleep(3)
        botao_cadastro = browser.find_element(By.XPATH, '//*[@id="submit"]')
        botao_cadastro.click()
        sleep(3)
    browser.close()

