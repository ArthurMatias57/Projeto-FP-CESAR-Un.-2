import os; os.system('cls')

list_metas = []
nome_do_arquivo = "Metas_de_saude.txt"

def template():
    print("\n************************\n")
    return

def add_metas(list_metas,nova_meta):
    nova_meta = list_metas.append(nova_meta)
    return 0

def pop_metas(indice, list_metas):
    indice = list_metas.pop(indice)
    return 0

def done_metas(indice):
    list_metas[indice] = (f'{list_metas[indice]} OK')
    return 

def change_metas(indice):
    list_metas[indice] = (f'{list_metas[indice]} OK')
    return 

def clean_metas():
    with open (nome_do_arquivo, 'w') as arquivo:
        arquivo.write('')
    return


while True:
    escolha = int(input('Você deseja: [1] Adicionar, [2] Apagar, [3] Marcar como feito, [4] Alterar, [5] Mostrar, [6] Limpar, [7] Sair: '))

    match escolha:
        case 1 :
            os.system('cls')
            nova_meta = input('Digite sua nova meta: ')
            add_metas(list_metas, nova_meta)
            print(list_metas)
            with open (nome_do_arquivo, 'a') as arquivo:
                for nome in list_metas:
                    arquivo.write(f'{nome}\n')
            list_metas.clear()
        case 2 :
            os.system('cls')
            with open (nome_do_arquivo, 'r') as arquivo:
                list_metas = [linha.strip() for linha in arquivo]
            print(list_metas)
            clean_metas()
            indice = int(input('Digite o indice que deseja apagar: '))
            pop_metas(indice,list_metas)
            with open (nome_do_arquivo, 'w') as arquivo:
                for nome in list_metas:
                    arquivo.write(f'{nome}\n')
            list_metas.clear()
        case 3 :
            os.system('cls')
            with open (nome_do_arquivo, 'r') as arquivo:
                list_metas = [linha.strip() for linha in arquivo]
            indice = int(input('Digite o indice concluido: '))
            done_metas(indice)
            clean_metas()
            with open (nome_do_arquivo, 'w') as arquivo:
                for nome in list_metas:
                    arquivo.write(f'{nome}\n')
            list_metas.clear()
        case 4 :
            os.system('cls')
            ...
        case 5 :
            with open (nome_do_arquivo, 'r') as arquivo:
                list_metas = [linha.strip() for linha in arquivo]
            os.system('cls')
            template()
            for nome in list_metas:
                print(nome)
            template()
        case 6 :
            os.system('cls')
            clean_metas(list_metas)
        case 7 :
            os.system('cls')
            break
        case _:
            os.system('cls')
            ...
    if escolha == '0':
        break
    else:
        continue