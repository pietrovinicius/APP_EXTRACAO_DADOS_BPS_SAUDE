#25/10/2023 21:11:00
#@PLima
#APP - EXTRACAO DE DADOS DO SITE BPS SAUDE

#https://bps.saude.gov.br/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas 
import os
import datetime

def agora():
    agora = datetime.datetime.now()
    agora = agora.strftime("%d/%m/%Y %H:%M:%S")
    return str(agora)

def agora_limpo():
    agora_limpo = datetime.datetime.now()
    agora_limpo = agora_limpo.strftime("%d/%m/%Y %H:%M:%S")    
    agora_limpo = agora_limpo.replace(":", "_").replace("/", "_")
    return str(agora_limpo) 

def print_pausa(texto , tempo):
    print(f"{agora()} - {texto} - tempo de: {tempo}s...")
    time.sleep(tempo)

def renomear_ultimo_arquivo_download(nome_novo):
  # Obtém o caminho da pasta DOWNLOAD.
  caminho_pasta_download = os.path.join(os.path.expanduser("~"), "Downloads")
  print(f'Caminho da pasta download: {caminho_pasta_download}')

  # Obtém o nome do último arquivo inserido na pasta.
  arquivos_download = os.listdir(caminho_pasta_download)

  print("\n\nIterando arquivos da pasta download:")
  contador = 0
  for arquivo_download in arquivos_download:    
    #print(f"arquivo_download: {arquivo_download}[{contador}]")
    if arquivo_download == 'Geral_BPS.csv':
        # Obtém a extensão do arquivo.
        ultimo_arquivo_download = arquivos_download[contador]
        (nome_arquivo, extensao_arquivo) = os.path.splitext(ultimo_arquivo_download)
        # Renomeia o arquivo.
        os.rename(os.path.join(caminho_pasta_download, ultimo_arquivo_download),
                  os.path.join(caminho_pasta_download, nome_novo + extensao_arquivo))
        print(f'\n############# Renomeiar o arquivo para: {nome_novo}\n')  
    #else:
        #print(f'Ultimo arquivo não foi renomeado, pois se chama: {arquivo_download}')
    contador = contador + 1

# Retira os acentos das vogais
def remover_acentos(texto):
    caracteres_a_substituir = {
    "Á": "A",
    "Â": "A",
    "À": "A",
    "Ã": "A",    
    "É": "E",
    "Ê": "E",
    "Í": "I",
    "Î": "I",
    "Ó": "O",
    "Ô": "O",
    "Õ": "O",
    "Ú": "U",
    "Û": "U",
    "Ü": "U",
    "Ç": "C",
    "#": "",
    "*": "",
    "!": "",
    "@": "",
    "#": "",
    "$": "",
    "%": "",
    "&": "",
    ",": "",
    "/": "",
    "_": "",
    ":": ""
    } 
    for caractere_original, caractere_substituido in caracteres_a_substituir.items():
        texto = texto.strip()
        texto = texto.upper()
        texto = texto.replace(caractere_original, caractere_substituido)
    return texto

def deletar_todos_arquivos_download():
  """
  Deleta todos os arquivos da pasta Download.

  Returns:
    None.
  """
  # Obtém o caminho da pasta Download.
  caminho_pasta_download = os.path.join(os.path.expanduser("~"), "Downloads")

  # Obtém os arquivos da pasta.
  arquivos_download = os.listdir(caminho_pasta_download)

  # Deleta os arquivos.
  for arquivo_download in arquivos_download:
    os.remove(os.path.join(caminho_pasta_download, arquivo_download))

try:
    #se não existir o arquivo txt será criado
    if not os.path.exists("log.txt"):
            with open("log.txt" , "r+") as log:
                log.write("")
    #abrindo log txt para escrever o que ocorre nas etapas                        
    with open("log.txt" , "r+") as log:
        print("================================ INICIO ======================")
        log.write(f"\n{agora()}\n================================ INICIO ======================")  
        
        #Deletando todos os arquivos da pasta download:
        #deletar_todos_arquivos_download()
        #print_pausa('deletar_todos_arquivos_download();', 1)
        #log.write('\ndeletar_todos_arquivos_download();')

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
        print_pausa(f"Grupos: {grupos}\n" , 1)
        log.write(f'\nGrupos: {agora()}')
        #lendo todas as linhas da coluna A
        print_pausa("Bloco for - Selecionando coluna 'GRUPOS:';" , 1)
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
             #//*[@id="formItensBPS:j_id219"]/fieldset/div[2]/input
             print_pausa('Botao Gerar Planilha 001' , 2)
             log.write(f"\nBotao Gerar Planilha 001 - {agora()}")
             botao_gerar_plan001.click()

             #Botao de gerar planilha 002
             botao_gerar_plan002 = driver.find_element(By.XPATH, value='//*[@id="formItensBPS:j_id515"]/fieldset/div[2]/input')
             #//*[@id="formItensBPS:j_id515"]/fieldset/div[2]/input
             print_pausa('Botao Gerar Planilha 002' , 2)
             log.write(f"\nBotao Gerar Planilha 002 - {agora()}")
             botao_gerar_plan002.click()
            
             print_pausa('Renomeando ultimo arquivo gerado...' , 1)
             log.write('\nRenomeando ultimo arquivo gerado...')
             var_grupo = remover_acentos(var_grupo)
             var_grupo = var_grupo[:40]
             print_pausa(f'Limitando nome do grupo em 40 letras: {var_grupo}' , 1)
             log.write(f'\nLimitando nome do grupo em 40 letras: {var_grupo}')

             nome_arquivo_temp = var_grupo + ' ' + agora_limpo()
             renomear_ultimo_arquivo_download(nome_arquivo_temp)
             log.write(f'\nrenomear_ultimo_arquivo_download: {nome_arquivo_temp}')

             print_pausa('Aguarde 5s...' , 5)


        #TODO: EXTRAIR TODOS OS "Fornecido Por:"
        #TODO: Inserir todos os Medicamentos e Fornecido_por em planilha


        print_pausa('Pausa final' , 5)
        print("================================ FIM ======================")
        log.write(f"\n{agora()}\n================================ FIM ======================")
        #input()

except KeyboardInterrupt as keyboard:
        print(f"================================ KeyboardInterrupt: \n{keyboard}")    

except Exception as erro:
    print(f"================================ Error: \n{erro}")