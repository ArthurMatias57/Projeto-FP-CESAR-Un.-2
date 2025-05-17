import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Funcoes"))

from Funcoes.cadastro_eventos import registrar_evento
from Funcoes.metas_saude import metasDeSaude
from Funcoes.CRUD import CRUD
from Funcoes.SugestoesPersonalizadas import sugestoesPersonalizadas


def inicio():
    print("**********Vida PET***********")
    try:
        selecao = int(input("Selecione uma das opções: \n1- CRUD\n2- Metas de saúde\n3- Sugestões personalizadas\n4- Cadastro de eventos\nR:"))
        
        match selecao:
            case 1:
                CRUD()
            case 2:
                metasDeSaude()
            case 3:
                sugestoesPersonalizadas()
            case 4:
                registrar_evento()
            case _:
                print("Por favor, digite uma opção válida!")
    except ValueError:
        print("Comando não Reconhecido! Digite uma opção válida!")

inicio()
