#funções
import os
from dic import *

def add():
    Tadd["Titulo"] = input("Digite o nome da tarefa:")
    Tadd["Descrição"] = input("Adicione uma descrição para a tarefa:")
    print("Tarefa adicionada...")

    

    
    for valor in Tadd.items():
       print(f"Titulo:{valor}   Descrição: {valor}")

    return Tadd 

    
  

   


def limpa_console():
    os.system("pause")
    os.system("cls")
    
    return limpa_console