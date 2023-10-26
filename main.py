#25/10/2023 21:11:00
#@PLima
#APP - EXTRACAO DE DADOS DO SITE BPS SAUDE

#https://bps.saude.gov.br/

from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import time

def print_pausa(texto , tempo):
    print(f"{texto} - tempo de: {tempo}s...")
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
    driver.implicitly_wait(1.5)

    botao_login = driver.find_element(By.NAME, value = 'formLogin:txtEmail1')
    print_pausa('Field txt e-mail' , 2)    
    botao_login.send_keys("pietrovinicius@gmail.com")
    print_pausa('Botao de Login' , 2)

    botao_submit = driver.find_element(By.NAME, value= 'formLogin:btnAcessarConsultaPublica')
    botao_submit.click()
    print_pausa('Botao Acessar ConsultaPublica de Login' , 2)

    botao_relatorios = driver.find_element(By.XPATH, value='//*[@id="barraMenu"]/ul[1]/li/p')
    print_pausa('Botao Relatorios' , 2)
    botao_relatorios.click()

    botao_geral = driver.find_element(By.XPATH, value='//*[@id="barraMenu"]/ul[1]/li/ul/li[1]/a')
    print_pausa('Botao Geral' , 2)
    botao_geral.click()

    check_base_siag = driver.find_element(By.XPATH, value='//*[@id="formItensBPS:dados"]')
    print_pausa('Check Box Base SIAG' , 1)
    check_base_siag.click()
     
    #TODO: EXTRAIR TODOS OS GRUPOS
    #TESTE GRUPO 'ARTIGOS DE HIGIENE':
    list_grupo = driver.find_element(By.XPATH, value='//*[@id="formItensBPS:grupoCATMAT"]')
    print_pausa('List GRUPO' , 1)

    #TODO: Ler opção de arquivo CSV
    list_grupo.send_keys('ARTIGOS DE HIGIENE')
    print_pausa('ARTIGOS DE HIGIENE' , 1)

    botao_pesquisar = driver.find_element(By.XPATH , value='//*[@id="conteudo"]/div[1]/input')
    print_pausa('Botao Pesquisar' , 1 )
    botao_pesquisar.click()
    print_pausa('Aguardando retorno do click em Pesquisar' , 3)

    botao_gerar_plan001 = driver.find_element(By.XPATH, value='//*[@id="formItensBPS:j_id219"]/fieldset/div[2]/input')
    print_pausa('Botao Gerar Planilha 001' , 1)
    botao_gerar_plan001.click()

    botao_gerar_plan002 = driver.find_element(By.XPATH, value='//*[@id="formItensBPS:j_id515"]/fieldset/div[2]/input')
    print_pausa('Botao Gerar Planilha 002' , 1)
    botao_gerar_plan002.click()

    #TODO: EXTRAIR TODOS OS "Fornecido Por:"
    #TODO: Inserir todos os Medicamentos e Fornecido_por em planilha

    print_pausa('Pausa final' , 5)
    input()

except KeyboardInterrupt as keyboard:
        print(f"KeyboardInterrupt: {keyboard}")    
except Exception as erro:
    print(f"Error: {erro}")