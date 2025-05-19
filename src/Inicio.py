import sys

sys.path.append("Projeto-FP-CESAR-Un.-2\src")

from Funcoes.cadastro_eventos import registrar_evento
from Funcoes.metas_saude import metasDeSaude
from Funcoes.CRUD import CRUD
from Funcoes.SugestoesPersonalizadas import sugestoesPersonalizadas

def titulo_ascii_vida_pet():
    print("\033[95m██    ██ ██  ██████   █████  \033[0m")  # VIDA
    print("\033[95m██    ██ ██  ██   ██ ██   ██ \033[0m")
    print("\033[95m██    ██ ██  ██   ██ ███████ \033[0m")
    print("\033[95m ██  ██  ██  ██   ██ ██   ██ \033[0m")
    print("\033[95m  ████   ██  ██████  ██   ██ \033[0m")

    print()  # Espaço entre as palavras

    print("\033[94m██████╗ ███████╗████████╗\033[0m")  # PET
    print("\033[94m██╔══██╗██╔════╝╚══██╔══╝\033[0m")
    print("\033[94m██████╔╝█████╗     ██║   \033[0m")
    print("\033[94m██╔═══╝ ██╔══╝     ██║   \033[0m")
    print("\033[94m██║     ███████╗   ██║   \033[0m")
    print("\033[94m╚═╝     ╚══════╝   ╚═╝   \033[0m")
    print("\n")


def inicio():
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
titulo_ascii_vida_pet()
inicio()





