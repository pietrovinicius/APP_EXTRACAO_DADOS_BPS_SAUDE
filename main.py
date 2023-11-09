#25/10/2023 21:11:00
#@PLima
#APP - EXTRACAO DE DADOS DO SITE BPS SAUDE

#https://bps.saude.gov.br/

from selenium import webdriver
from selenium.webdriver.common.by import By
#import openpyxl
import time
import pandas 
import os
import datetime

def agora():
    agora = datetime.datetime.now()
    agora = agora.strftime("%d/%m/%Y %H:%M:%S")
    return str(agora)  

def print_pausa(texto , tempo):
    print(f"{agora()} - {texto} - tempo de: {tempo}s...")
    time.sleep(tempo)        

try:
    print("================================ INICIO ======================")

    #se não existir o arquivo txt será criado
    if not os.path.exists("log.txt"):
            with open("log.txt" , "r+") as log:
                log.write("")
    #abrindo log txt para escrever o que ocorre nas etapas                        
    with open("log.txt" , "r+") as log:
        log.write(f"\nLOG agora: {agora()}")            
        print(f"LOG agora: {agora()}")    

        driver = webdriver.Chrome()
        #driver.get("https://2252tst1wecare.cloudmv.com.br/pronep")
        driver.get("http://bps.saude.gov.br/visao/consultaPublica/index.jsf")
        title = driver.title
        driver.implicitly_wait(1.5)

        botao_login = driver.find_element(By.NAME, value = 'formLogin:txtEmail1')
        print_pausa('Field txt e-mail' , 2)    
        log.write(f"\nField txt e-mail: {agora()}")

        botao_login.send_keys("pietrovinicius@gmail.com")
        print_pausa('Botao de Login send_keys("pietrovinicius@gmail.com"): ' , 2)
        log.write(f'\nBotao de Login send_keys("pietrovinicius@gmail.com"): {agora()}')

        botao_submit = driver.find_element(By.NAME, value= 'formLogin:btnAcessarConsultaPublica')
        botao_submit.click()
        print_pausa('Botao Acessar ConsultaPublica de Login' , 2)
        log.write(f'\nBotao Acessar ConsultaPublica de Login: {agora()}')

        botao_relatorios = driver.find_element(By.XPATH, value='//*[@id="barraMenu"]/ul[1]/li/p')
        print_pausa('Botao Relatorios' , 2)
        log.write(f'\nBotao Relatorios: {agora()}')
        botao_relatorios.click()

        botao_geral = driver.find_element(By.XPATH, value='//*[@id="barraMenu"]/ul[1]/li/ul/li[1]/a')
        print_pausa('Botao Geral' , 2)
        log.write(f'\nBotao Geral: {agora()}')
        botao_geral.click()

        check_base_siag = driver.find_element(By.XPATH, value='//*[@id="formItensBPS:dados"]')
        print_pausa('Check Box Base SIAG' , 1)
        log.write(f'\nCheck Box Base SIAG: {agora()}')
        check_base_siag.click()

        #TODO: EXTRAIR TODOS OS GRUPOS
        print_pausa('Abrindo planilha()\npandas.read_excel("grupo.xlsx" , sheet_name="grupo")', 1)
        log.write(f'\nAbrindo planilha()\npandas.read_excel("grupo.xlsx" , sheet_name="grupo")')
        #abrindo_planilha()
        grupos = pandas.read_excel("grupo.xlsx", sheet_name="grupo")
        print_pausa(f"Grupos: {grupos}" , 1)
        log.write(f'\nGrupos: {agora()}')
        #lendo todas as linhas da coluna A
        print_pausa("Bloco for\nSelecionando coluna 'GRUPOS:';" , 1)
        var_grupo = ""
        for dados in grupos.index:
             #valor obtido da coluna com a primeira linha 'GRUPOS:' 
             var_grupo = grupos.loc[dados, "GRUPOS:"]
             print_pausa(f"Variavel var_grupo: {var_grupo}" , 1)
             log.write(f"\nGrupo: {var_grupo} - {agora()}")

             #SELECIONANDO COMPONENTE DE SELEÇÃO DOS GRUPOS:
             list_grupo = driver.find_element(By.XPATH, value='//*[@id="formItensBPS:grupoCATMAT"]')
             print_pausa('List GRUPO' , 1)
             log.write(f"\nList Grupo - {agora()}")

             #enviando valor obtido na coluna GRUPOS da planilha:
             list_grupo.send_keys(var_grupo)
             print_pausa(f"send_keys: {var_grupo}", 1)
             log.write(f"\nsend_keys: {var_grupo} - {agora()}")

             botao_pesquisar = driver.find_element(By.XPATH , value='//*[@id="conteudo"]/div[1]/input')
             print_pausa('Botao Pesquisar' , 1 )
             log.write(f"\nBotao Pesquisar - {agora()}")

             botao_pesquisar.click()
             print_pausa('Aguardando retorno do click em Pesquisar' , 3)
             log.write(f"\nAguardando retorno do click em Pesquisar - {agora()}")

             #Botao de gerar planilha 001
             botao_gerar_plan001 = driver.find_element(By.XPATH, value='//*[@id="formItensBPS:j_id219"]/fieldset/div[2]/input')
             print_pausa('Botao Gerar Planilha 001' , 2)
             log.write(f"\nBotao Gerar Planilha 001 - {agora()}")
             botao_gerar_plan001.click()

             #Botao de gerar planilha 002
             botao_gerar_plan002 = driver.find_element(By.XPATH, value='//*[@id="formItensBPS:j_id515"]/fieldset/div[2]/input')
             #//*[@id="formItensBPS:j_id515"]/fieldset/div[2]/input
             print_pausa('Botao Gerar Planilha 002' , 2)
             log.write(f"\nBotao Gerar Planilha 002 - {agora()}")
             botao_gerar_plan002.click()


        #TODO: EXTRAIR TODOS OS "Fornecido Por:"
        #TODO: Inserir todos os Medicamentos e Fornecido_por em planilha


        print_pausa('Pausa final' , 5)
        print("================================ FIM ======================")
        log.write(f"\n================================ FIM ======================")
        #input()

except KeyboardInterrupt as keyboard:
        print(f"================================ KeyboardInterrupt: \n{keyboard}")    

except Exception as erro:
    print(f"================================ Error: \n{erro}")