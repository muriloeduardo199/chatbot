import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

file_csv= pd.read_csv("/home/murilo/Área de Trabalho/teste.csv")

driver = webdriver.Chrome("caminho_para_o_WebDriver")

driver.get("https://web.whatsapp.com")
input("Faça login no WhatsApp Web e pressione Enter para continuar...")

for files in file_csv["Celular"]:
    link = f"https://web.whatsapp.com/send?phone={files}"
    driver.get(link)
    time.sleep(5)
    
    campo_mensagem = driver.find_element(By.CLASS_NAME, "_3Uu1_")
    
    mensagem = "A SulAmérica está com uma promoção imperdível no plano de saúde Direto Aracaju. Aproveite. É por tempo limitado. Quer saber mais? Diga sim."
    
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)
    
    time.sleep(5)

    ## Localizar o botão de anexar arquivo ou imagem
    botao_anexo = driver.find_element(By.XPATH, "//div[@title='Anexar']")
    botao_anexo.click()

    # Aguardar um breve período para a janela de seleção de arquivo ser exibida
    time.sleep(2)

    # Inserir o caminho do arquivo da imagem que você deseja enviar
    campo_arquivo = driver.find_element(By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
    campo_arquivo.send_keys("/home/murilo/Área de Trabalho/imagem_rami.jpeg")  # Substitua pelo caminho da imagem desejada

    # Aguardar 5 segundos para a imagem ser enviada
    time.sleep(5)

    # Localizar o botão de envio
    botao_enviar = driver.find_element(By.XPATH, "//span[@data-icon='send']")
    botao_enviar.click()

driver.quit()

















