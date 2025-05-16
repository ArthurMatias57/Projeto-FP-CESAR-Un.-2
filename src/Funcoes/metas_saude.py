from src.BD import Metas_de_saude
import os; 
#os.system('clear')

list_metas = []
aux_metas = []
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

def change_metas(indice, nova_meta):
    list_metas[indice] = (f'{nova_meta}')
    return 

def clean_metas():
    with open (nome_do_arquivo, 'w') as arquivo:
        arquivo.write('')
    return

def metasDeSaude():
    while True:
        
        try:
            escolha = int(input('[1] Adicionar\n[2] Apagar\n[3] Marcar como feito\n[4] Alterar\n[5] Mostrar\n[6] Limpar\n[7] Sair\nVocê deseja: '))

        except ValueError:
            print('O valor esperado são valores entre 1 e 7')
            os.system('clear')
            

        match escolha:
            case 1 :
                os.system('clear')
                try:
                    nova_meta = input('Digite sua nova meta: ')
                    add_metas(list_metas, nova_meta)
                    print(list_metas)
                    with open (nome_do_arquivo, 'a') as arquivo:
                        for nome in list_metas:
                            arquivo.write(f'{nome}\n')
                    list_metas.clear()
                except ValueError:
                    print('Valor incorreto, tente novamente.')
                except FileNotFoundError:
                    print('Arquivo não foi encontrada.')
                except Exception as e:
                    print('Ocorreu um erro inesperado.')

            case 2 :
                os.system('clear')
                try:
                    with open (nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
                        list_metas = [linha.strip() for linha in arquivo]
                    print(list_metas)
                    indice = int(input('Digite o indice que deseja apagar: '))
                    if indice in range(len(list_metas)):
                        clean_metas()
                        pop_metas(indice,list_metas)
                        with open (nome_do_arquivo, 'w') as arquivo:
                            for nome in list_metas:
                                arquivo.write(f'{nome}\n')
                                aux_metas.append(nome)
                        list_metas.clear()
                    else:
                        print('Não existe meta com esse índice!')
                        continue
                except FileNotFoundError:
                    print('Pagina não encontrada.')
                except ValueError:
                    print('Você precisa colocar um valor inteiro')
                except IndexError:
                    print('Esse indice não existe.')

            case 3 :
                try:
                    os.system('clear')
                    with open (nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
                        list_metas = [linha.strip() for linha in arquivo]
                    indice = int(input('Digite o indice concluido: '))
                    done_metas(indice)
                    clean_metas()
                    with open (nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
                        for nome in list_metas:
                            arquivo.write(f'{nome}\n')
                    list_metas.clear()
                except FileNotFoundError:
                    print('Pagina não encontrada.')
                except ValueError:
                    print('Você precisa colocar um valor inteiro')
                except IndexError:
                    print('Esse indice não existe.')
                    
            case 4 :
                try:
                    os.system('clear')
                    with open (nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
                        list_metas = [linha.strip() for linha in arquivo]
                    indice = int(input('Digite o índice que deseja alterar: '))
                    nova_meta = input('Digite sua nova meta: ')
                    change_metas(indice, nova_meta)
                    clean_metas()
                    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
                        for nome in list_metas:
                            arquivo.write(f'{nome}\n')
                        list_metas.clear()
                except FileNotFoundError:
                    print('Pagina não encontrada.')
                except ValueError:
                    print('Você precisa colocar um valor inteiro')
                except IndexError:
                    print('Esse indice não existe.')

            case 5 :
                try:
                    os.system('clear')
                    with open (nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
                        list_metas = [linha.strip() for linha in arquivo]
                    template()
                    for nome in list_metas:
                        print(nome)
                    template()
                except FileNotFoundError:
                    print('Pagina não encontrada.')
            case 6 :
                os.system('clear')
                clean_metas()
            case 7 :
                os.system('clear')
                break
            case _:
                os.system('clear')
                print('Entrada válidas: [1] até [8]')
                continue
        if escolha == False:
            break
        else:
            continue
