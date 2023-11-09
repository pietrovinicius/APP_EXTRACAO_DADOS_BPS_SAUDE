#08/11/2023 21:11:00
#@PLima
#APP - EXTRACAO DE DADOS DO SITE BPS SAUDE
#Classe teste de leitura de planilha xslx


#import pandas
import pandas 


try:
    print("\n\n=========================== INICIO ===========================")
    print("Bloco Try")
    
    print("Abrindo planilha()")
    print('pandas.read_excel("grupo.xlsx" , sheet_name="grupo")')
    #abrindo_planilha()
    grupos = pandas.read_excel("grupo.xlsx", sheet_name="grupo")
    print(f"Grupos: {grupos}")
    #lendo todas as linhas da coluna A
    print("Bloco for\nSelecionando coluna 'GRUPOS:';")
    var_grupo = ""
    for dados in grupos.index:
         #valor obtido da coluna com a primeira linha 'GRUPOS:' 
         var_grupo = grupos.loc[dados, "GRUPOS:"]
         print(f"Variavel var_grupo: {var_grupo}")
    

except KeyboardInterrupt as keyboard:
        print(f"KeyboardInterrupt: {keyboard}")    
except Exception as erro:
    print(f"Error: {erro}")

#abertura de planilha

#array com cada opção digitada na coluna da planilha