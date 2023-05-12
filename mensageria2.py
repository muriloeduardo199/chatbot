import pyautogui as pg
import webbrowser as web
import time
import pandas as pd



data = pd.read_csv("/home/murilo/Área de Trabalho/teste.csv")
data
data_dict = data.to_dict('list')

leads = data_dict['Celular']
messages = data_dict['texto']
combo = zip(leads,messages)
first = True
for lead,message in combo:
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+str(lead)+"&text="+ str(message))
    if first:
        time.sleep(6)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('esc')
    time.sleep(5)
    pg.press('enter')
    time.sleep(10)
    pg.hotkey('ctrl', 'w')