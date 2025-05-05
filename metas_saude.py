# import os; os.system('cls')

# dic_metas = {}

# nome_do_arquivo = "Metas_de_saude.txt"
# def template():
#     print("\n************************\n")
#     return

# def nova_meta(adicionar_meta):
#     with open("Metas_de_saude.txt", "a") as arquivo:
#         arquivo.write(f'{adicionar_meta}\n')
#     return ()

# def ler_meta():
#     with open(nome_do_arquivo) as arquivo:
#         print(arquivo.read())
#     return(ler_meta)

# def limpar_meta():
#     with open(nome_do_arquivo, "w") as arquivo:
#         arquivo.write('')
# def apagar_meta(indice_linha, nome_do_arquivo):
#     try:
#         with open(nome_do_arquivo, "r") as arquivo:
#             linhas = arquivo.readlines()

#             linha.pop(indice_linha)
#         with open(nome_do_arquivo, "w") as arquivo:
#             for linha in linhas:
#                 arquivo.write(linha)
#         print(f"Linha {indice_linha + 1} removida com sucesso do arquivo {nome_do_arquivo}.")
            
#     except FileNotFoundError:
#         print(f"Erro: Arquivo '{nome_do_arquivo}' não encontrado.")
#     except IndexError:
#         print(f"Erro: Índice da linha inválido.")
#     except Exception as e:
#         print(f"Erro: {e}")
# # def feito_meta(numero_da_linha):
# #     try:
# #         with open(nome_do_arquivo, 'r') as arquivo:
# #             linhas = arquivo.readlines()

# #         if 1 <= numero_da_linha <= len(linhas):
# #             linhas[numero_da_linha - 1] = nova_linha + '\n'  # Adicionar o caractere de nova linha

# #         with open(nome_do_arquivo, 'w') as arquivo:
# #             arquivo.writelines(linhas)
# #     except FileNotFoundError:
# #         print(f"Arquivo '{nome_do_arquivo}' não encontrado.")
# #     except Exception as e:
# #         print(f"Ocorreu um erro: {e}")
        
# while True:
#     escolha = int(input('Você deseja: [1] Adicionar, [2] Apagar, [3] Marcar como feito, [4] Alterar, [5] Mostrar, [6] Limpar, [7] Sair: '))

#     match escolha:
#         case 1 :
#             os.system('cls')
#             adicionar_meta = input('Digite sua meta:')
#             nova_meta(adicionar_meta)
#             template()
#             print(f'Meta: | {adicionar_meta} | adicionada!')
#             template()
#         case 2 :
#             os.system('cls')
#             indice_linha = input('Digite qual linha deseja apagar.')
#             apagar_meta(indice_linha, nome_do_arquivo)
#         case 3 :
#             os.system('cls')
#             with open(nome_do_arquivo, "r") as arquivo:
#                 print(arquivo.readlines())
#             with open(nome_do_arquivo, 'x') as arquivo:
#                 indice_linha = int(input('Digite qual linha deseja apagar.'))
#                 apaga = arquivo.readlines(indice_linha)
#                 del apaga
#                 print(arquivo.readlines())
#         case 4 :
#             os.system('cls')
#             ...
#         case 5 :
#             os.system('cls')
#             ...
#         case 6 :
#             os.system('cls')
#             limpar_meta()
#             template()
#             print('Metas Limpas!')
#             template()
#         case 7 :
#             os.system('cls')
#             break
#         case _:
#             os.system('cls')
#             template()
#             print('Escolha inválida, tente novamente!')
#             template()
#     if nova_meta == '0':
#         break
#     else:
#         continue