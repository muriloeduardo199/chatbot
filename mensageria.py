import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Caminho para o Chrome WebDriver
webdriver_path = '/caminho/para/chromedriver'

# Localização do arquivo CSV
csv_file = '/home/murilo/Área de Trabalho/teste.csv'

# Inicializa o driver do Chrome
options = Options()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(executable_path=webdriver_path, options=options)

# Abre o WhatsApp Web
driver.get('https://web.whatsapp.com/')
print("Aguarde a leitura do código QR...")

# Aguarda a leitura do código QR manualmente
input("Pressione Enter após fazer login no WhatsApp Web.")

# Função para enviar mensagem para um contato
def send_message(phone_number, message):
    driver.get(f'https://web.whatsapp.com/send?phone={phone_number}&text={message}')
    time.sleep(5)  # Aguarda um tempo para carregar a página
    try:
        send_button = driver.find_element("//span[@data-testid='send']")
        send_button.click()
        print(f"Mensagem enviada para {phone_number}: {message}")
    except:
        print(f"Falha ao enviar mensagem para {phone_number}")

# Lê o arquivo CSV e envia as mensagens
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        phone_number = row['Primeiro Nome']
        message = row['Celular']
        send_message(phone_number, message)

# Encerra o driver
driver.quit()
