from cadastro_eventos import *
from metas_saude import *
from CRUD import *
from SugestoesPersonalizadas import *

def inicio():
    print("Vida PET")
    selecao = int(input("Selecione uma das opções: \n1- CRUD\n2- Metas de saúde\n3- Sugestões personalizadas\n4- Cadastro de eventos"))
    match selecao:
        case 1:
            CRUD()
        case 2:
            metasDeSaude()
        case 3:
            sugestoesPersonalizadas()
        case 4:
            registrar_evento()
inicio()
