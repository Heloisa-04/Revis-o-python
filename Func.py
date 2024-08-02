#funções
import os 

def menu():
    print("--MENU--")
    print("1 - ADICIONAR TAREFAS")
    print("2 - EDITAR TAREFAS")
    print("3 - EXCLUIR TAREFAS")
    print("4 - SAIR")

    escolha=int(input("Qual opção deseja? \n -->"))
    return escolha


def limpa_console():
    os.system("pause")
    os.system("cls")
    
    return limpa_console