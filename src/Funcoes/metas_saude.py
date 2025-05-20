import os
import sys

#Importação funções globais
CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "..", "BD", "Metas_de_saude.txt")
sys.path.append("Projeto-FP-CESAR-Un.-2\src\FuncoesGlobais.py") 
from FuncoesGlobais import *


def add_metas(list_metas, nova_meta):
    list_metas.append(nova_meta)
    print(f"Meta '{nova_meta}' adicionada com sucesso!")
    lin()

def pop_metas(indice, list_metas):
    if 0 <= indice < len(list_metas):
        meta_removida = list_metas.pop(indice)
        print(f"Meta '{meta_removida}' removida com sucesso!")
    else:
        print("Índice inválido!")
    lin()

def done_metas(indice):
    try:
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            list_metas = [linha.strip() for linha in arquivo]
        
        if 0 <= indice < len(list_metas):
            meta_concluida = list_metas[indice]
            list_metas[indice] = f"[CONCLUÍDO] {meta_concluida}" if not meta_concluida.startswith("[CONCLUÍDO]") else meta_concluida
            
            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
                for meta in list_metas:
                    arquivo.write(f"{meta}\n")
            
            print(f"Meta marcada como concluída!")
        else:
            print("Índice inválido!")
        lin()
    except FileNotFoundError:
        print("Arquivo de metas não encontrado!")
        lin()
    except Exception as e:
        print(f"Erro ao marcar meta como concluída: {e}")
        lin()

def change_metas(indice, nova_meta):
    try:
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            list_metas = [linha.strip() for linha in arquivo]
        
        if 0 <= indice < len(list_metas):
            meta_antiga = list_metas[indice]
            list_metas[indice] = nova_meta
            
            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
                for meta in list_metas:
                    arquivo.write(f"{meta}\n")
            
            print(f"Meta alterada de '{meta_antiga}' para '{nova_meta}'!")
        else:
            print("Índice inválido!")
        lin()
    except FileNotFoundError:
        print("Arquivo de metas não encontrado!")
        lin()
    except Exception as e:
        print(f"Erro ao alterar meta: {e}")
        lin()

def clean_metas():
    try:
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            arquivo.write("")
        print("Todas as metas foram removidas!")
        lin()
    except Exception as e:
        print(f"Erro ao limpar as metas: {e}")
        lin()

def metasDeSaude():
    # Garantir que o arquivo existe
    os.makedirs(os.path.dirname(CAMINHO_ARQUIVO), exist_ok=True)
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8'):
            pass
    
    list_metas = []
    
    while True:
        lin()
        print("METAS DE SAÚDE PARA SEU PET")
        lin()
        
        try:
            escolha_input = input('[1] Adicionar\n[2] Apagar\n[3] Marcar como feito\n[4] Alterar\n[5] Mostrar\n[6] Limpar\n[7] Sair\nVocê deseja: ').strip()
            if not escolha_input:
                print('Por favor, digite uma opção.')
                continue
                
            escolha = int(escolha_input)
            
            if escolha < 1 or escolha > 7:
                print('O valor esperado são valores entre 1 e 7')
                continue
        except ValueError:
            print('Por favor, digite um número válido entre 1 e 7')
            continue

        match escolha:
            case 1:
                while True:
                    nova_meta = input('Digite sua nova meta: ').strip()
                    if nova_meta:
                        break
                    print("A meta não pode estar vazia.")
                
                add_metas(list_metas, nova_meta)
                with open(CAMINHO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
                    arquivo.write(f'{nova_meta}\n')
                list_metas.clear()

            case 2:
                try:
                    with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                        list_metas = [linha.strip() for linha in arquivo]
                    
                    if not list_metas:
                        print("Não há metas cadastradas!")
                        continue
                        
                    print("Metas disponíveis:")
                    for i, meta in enumerate(list_metas):
                        print(f"[{i}] {meta}")
                    
                    try:
                        indice_input = input('Digite o índice que deseja apagar: ').strip()
                        if not indice_input:
                            print("O índice não pode estar vazio.")
                            continue
                            
                        indice = int(indice_input)
                        if indice in range(len(list_metas)):
                            pop_metas(indice, list_metas)
                            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
                                for meta in list_metas:
                                    arquivo.write(f'{meta}\n')
                        else:
                            print("Índice inválido!")
                    except ValueError:
                        print("Por favor, digite um número válido!")
                except Exception as e:
                    print(f"Erro ao apagar meta: {e}")
                list_metas.clear()

            case 3:
                try:
                    with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                        list_metas = [linha.strip() for linha in arquivo]
                    
                    if not list_metas:
                        print("Não há metas cadastradas!")
                        continue
                        
                    print("Metas disponíveis:")
                    for i, meta in enumerate(list_metas):
                        print(f"[{i}] {meta}")
                    
                    try:
                        indice_input = input('Digite o índice concluído: ').strip()
                        if not indice_input:
                            print("O índice não pode estar vazio.")
                            continue
                            
                        indice = int(indice_input)
                        done_metas(indice)
                    except ValueError:
                        print("Por favor, digite um número válido!")
                except Exception as e:
                    print(f"Erro ao marcar meta como concluída: {e}")
                list_metas.clear()

            case 4:
                try:
                    with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                        list_metas = [linha.strip() for linha in arquivo]
                    
                    if not list_metas:
                        print("Não há metas cadastradas!")
                        continue
                        
                    print("Metas disponíveis:")
                    for i, meta in enumerate(list_metas):
                        print(f"[{i}] {meta}")
                    
                    try:
                        indice_input = input('Digite o índice que deseja alterar: ').strip()
                        if not indice_input:
                            print("O índice não pode estar vazio.")
                            continue
                            
                        indice = int(indice_input)
                        if indice in range(len(list_metas)):
                            while True:
                                nova_meta = input('Digite sua nova meta: ').strip()
                                if nova_meta:
                                    break
                                print("A meta não pode estar vazia.")
                                
                            change_metas(indice, nova_meta)
                        else:
                            print("Índice inválido!")
                    except ValueError:
                        print("Por favor, digite um número válido!")
                except Exception as e:
                    print(f"Erro ao alterar meta: {e}")
                list_metas.clear()

            case 5:
                try:
                    with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                        list_metas = [linha.strip() for linha in arquivo]
                    
                    lin()
                    if not list_metas:
                        print("Não há metas cadastradas!")
                    else:
                        print("SUAS METAS DE SAÚDE:")
                        for i, meta in enumerate(list_metas):
                            print(f"[{i}] {meta}")
                    lin()
                except Exception as e:
                    print(f"Erro ao mostrar metas: {e}")

            case 6:
                confirmacao = input("Tem certeza que deseja limpar todas as metas? (s/n): ").lower()
                if confirmacao == 's':
                    clean_metas()
                else:
                    print("Operação cancelada!")

            case 7:
                menuSairOuReinicio(metasDeSaude)
                return

            case _:
                print('Entrada válida: [1] até [7]')
#metasDeSaude()