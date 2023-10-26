#25/10/2023 21:11:00
#@PLima
#APP - EXTRACAO DE DADOS DO SITE BPS SAUDE

#https://bps.saude.gov.br/

from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import time

def pausa(texto , tempo):
    print(f"{texto} - pausa de: {tempo}s...")
    time.sleep(tempo)

    
#1) FORNECIDO POR:
#   //td[@class="scGridFieldOddFont css_fornecidopor_grid_line"]
#2) PRODUTO:
#   //td[@class="scGridFieldOddFont css_classificacaoservico_grid_line"]

#ENCONTRANDO NA PAGINA TODOS OS ELEMENTOS QUE CONTENHAM A DESCRIÇÃO DO PRODUTO:

try:
    print("================================ INICIO ======================")    
    #acessar o site: https://2252tst1wecare.cloudmv.com.br/pronep
    #print("Acessar o site: https://2252tst1wecare.cloudmv.com.br/pronep")

    driver = webdriver.Chrome()
    #driver.get("https://2252tst1wecare.cloudmv.com.br/pronep")
    driver.get("http://bps.saude.gov.br/visao/consultaPublica/index.jsf")
    title = driver.title
    driver.implicitly_wait(1)

    botao_login = driver.find_element(By.NAME, value = 'formLogin:txtEmail1')
    pausa('Field txt e-mail' , 2)    
    botao_login.send_keys("pietrovinicius@gmail.com")
    pausa('Botao de Login' , 2)

    botao_submit = driver.find_element(By.NAME, value= 'formLogin:btnAcessarConsultaPublica')
    botao_submit.click()
    pausa('Botao Acessar ConsultaPublica de Login' , 2)

    botao_relatorios = driver.find_element(By.XPATH, value='//*[@id="barraMenu"]/ul[1]/li/p')
    pausa('Botao Relatorios' , 2)
    botao_relatorios.click()

    botao_geral = driver.find_element(By.XPATH, value='//*[@id="barraMenu"]/ul[1]/li/ul/li[1]/a')
    pausa('Botao Geral' , 2)
    botao_geral.click()
     
    #TODO: EXTRAIR TODOS OS PRODUTOS "Medicamento"
    #TODO: EXTRAIR TODOS OS "Fornecido Por:"
    #TODO: Inserir todos os Medicamentos e Fornecido_por em planilha

    pausa('Pausa final' , 5)
    input()

except KeyboardInterrupt as keyboard:
        print(f"KeyboardInterrupt: {keyboard}")    
except Exception as erro:
    print(f"Error: {erro}")