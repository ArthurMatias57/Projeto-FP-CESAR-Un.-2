import os

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "..", "BD", "Metas_de_saude.txt")

"""
def menuSairOuReinicio():
    while True:
        final = input("O que você deseja fazer agora?\n"
                      "1 - \n"
                      "2 - Voltar ao menu principal\n"
                      "\nEscolha: ").strip().lower()
        lin()

        if final == 1:
            # Deve retornar a funcionalidade
            Ex: CRUD()
        elif final == 2 :
            print("Voltando ao menu principal")
            inicio()
            exit()
        else:
            print("Opção inválida. Tente novamente.")

"""

list_metas = []
aux_metas = []

def template():
    print("\n************************\n")
    return

def add_metas(list_metas, nova_meta):
    list_metas.append(nova_meta)
    return 0

def pop_metas(indice, list_metas):
    list_metas.pop(indice)
    return 0

def done_metas(indice):
    list_metas[indice] = f'{list_metas[indice]} OK'
    return 

def change_metas(indice, nova_meta):
    list_metas[indice] = nova_meta
    return 

def clean_metas():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        arquivo.write('')
    return

def metasDeSaude():
    list_metas = []
    aux_metas = []


    while True:
        try:
            escolha = int(input('[1] Adicionar\n[2] Apagar\n[3] Marcar como feito\n[4] Alterar\n[5] Mostrar\n[6] Limpar\n[7] Sair\nVocê deseja: '))
        except ValueError:
            print('O valor esperado são valores entre 1 e 7')
            continue

        match escolha:
            case 1:
                nova_meta = input('Digite sua nova meta: ')
                add_metas(list_metas, nova_meta)
                with open(CAMINHO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
                    for nome in list_metas:
                        arquivo.write(f'{nome}\n')
                list_metas.clear()

            case 2:
                with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                    list_metas = [linha.strip() for linha in arquivo]
                print(list_metas)
                indice = int(input('Digite o indice que deseja apagar: '))
                if indice in range(len(list_metas)):
                    clean_metas()
                    pop_metas(indice, list_metas)
                    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
                        for nome in list_metas:
                            arquivo.write(f'{nome}\n')
                            aux_metas.append(nome)
                    list_metas.clear()

            case 3:
                with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                    list_metas = [linha.strip() for linha in arquivo]
                indice = int(input('Digite o indice concluido: '))
                done_metas(indice)
                clean_metas()
                with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
                    for nome in list_metas:
                        arquivo.write(f'{nome}\n')
                list_metas.clear()

            case 4:
                with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                    list_metas = [linha.strip() for linha in arquivo]
                indice = int(input('Digite o índice que deseja alterar: '))
                nova_meta = input('Digite sua nova meta: ')
                change_metas(indice, nova_meta)
                clean_metas()
                with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
                    for nome in list_metas:
                        arquivo.write(f'{nome}\n')
                list_metas.clear()

            case 5:
                with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                    list_metas = [linha.strip() for linha in arquivo]
                template()
                for nome in list_metas:
                    print(nome)
                template()

            case 6:
                clean_metas()

            case 7:
                break

            case _:
                print('Entrada válida: [1] até [7]')
#metasDeSaude()