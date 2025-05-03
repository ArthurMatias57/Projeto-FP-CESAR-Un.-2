import os; os.system('cls')

def template():
    print("\n************************\n")
    return

def nova_meta(adicionar_meta):
    with open("Metas_de_saude.txt", "a") as arquivo:
        arquivo.write(f'{adicionar_meta}\n')
    return ()

def ler_meta():
    with open("Metas_de_saude.txt") as arquivo:
        print(arquivo.read())
    return(ler_meta)

def limpar_meta():
    with open("Metas_de_saude.txt", "w") as arquivo:
        arquivo.write('')

def apagar_meta():
    with open("Metas_de_saude.txt", "r") as arquivo:
        linhas = arquivo.readlines()

while True:
    escolha = int(input('Você deseja: [1] Adicionar, [2] Apagar, [3] Marcar como feito, [4] Alterar, [5] Mostrar, [6] Limpar, [7] Sair: '))

    match escolha:
        case 1 :
            os.system('cls')
            adicionar_meta = input('Digite sua meta:')
            nova_meta(adicionar_meta)
            template()
            print(f'Meta: | {adicionar_meta} | adicionada!')
            template()
        case 2 :
            os.system('cls')
            nova_meta()
        case 3 :
            os.system('cls')
            ...
        case 4 :
            os.system('cls')
            ...
        case 5 :
            os.system('cls')
            ...
        case 6 :
            os.system('cls')
            limpar_meta()
            template()
            print('Metas Limpas!')
            template()
        case 7 :
            os.system('cls')
            break
        case _:
            os.system('cls')
            template()
            print('Escolha inválida, tente novamente!')
            template()
    if nova_meta == '0':
        break
    else:
        continue