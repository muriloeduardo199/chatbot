import pandas as pd
import selenium
from selenium.webdriver.common.keys import Keys
import time
import urllib
from selenium import webdriver


contatos_df = pd.read_excel("Enviar.xlsx", engine='openpyxl')

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)


# já estamos com o login feito no whatsapp web





    navegador.find_element_by_css_selector('#main > footer > div._2BU3P.tm2tP.copyable-area > div._1SEwr > div > div._3HQNh._1Ae7k').click()
    

    time.sleep(10)



















