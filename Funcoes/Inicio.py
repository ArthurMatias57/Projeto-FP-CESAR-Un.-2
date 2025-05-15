import Funcoes
import Funcoes.SugestoesPersonalizadas
import Funcoes.cadastro_eventos
import Funcoes.metas_saude

def inicio():
    print("Vida PET")
    selecao = int(input("Selecione uma das opções: \n1- CRUD\n2- Metas de saúde\n3- Sugestões personalizadas\n4- Cadastro de eventos"))
    match selecao:
        case 1:
            Funcoes.CRUD.CRUD()
        case 2:
            Funcoes.metas_saude.metasDeSaude()
        case 3:
            Funcoes.SugestoesPersonalizadas.sugestoesPersonalizadas()
        case 4:
            Funcoes.cadastro_eventos.registrar_evento()
inicio()
print("BCt")