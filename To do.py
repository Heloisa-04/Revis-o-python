#Criar tarefas
#Excluir tarefas
#Editar tarefas


import os 
from Func import *

sair = 0 
list_dic = [Tadd]

while sair == 0:
    print("Gerenciador de tarefas - TO DO")
    print("     --MENU--    ")
    print("1 - ADICIONAR TAREFAS")
    print("2 - EDITAR TAREFAS")
    print("3 - EXCLUIR TAREFAS")
    print("4 - SAIR")

    escolha=int(input("Qual opção deseja? \n -->"))
    limpa_console()
    

    if escolha == 1:
        add()
        limpa_console()


    elif escolha == 2:
        pass

    elif escolha == 3:
        pass

    elif escolha == 4:
        sair = 1
        print("Saindo...")
    
    else:
        escolha = 0
        print("Opção inválida")
        

os.system("pause")