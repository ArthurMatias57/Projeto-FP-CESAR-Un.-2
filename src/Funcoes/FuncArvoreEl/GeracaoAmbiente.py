import os
import sys
import time
import unicodedata

CAMINHO_AMBIENTE = os.path.join("Projeto-FP-CESAR-Un.-2\src\BD\BDambiente.txt")
#Importação funções globais
sys.path.append("Projeto-FP-CESAR-Un.-2\src")
from FuncoesGlobais import *


def criar_arvore(caminho_arquivo):
    arvore = {}
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            if linha.strip().startswith("#") or not linha.strip():
                continue  # Ignora comentários e linhas vazias
            dados = linha.strip().split('|')
            if len(dados) != 7:
                continue  # Ignora linhas mal formatadas
            raca, grupo, especie, nome_pop, caracteristicas, rec_gen, rec_esp = dados
            caracteristicas = [c.strip().lower() for c in caracteristicas.split(',')]

            if raca not in arvore:
                arvore[raca] = {"grupos": {}}
            if grupo not in arvore[raca]["grupos"]:
                arvore[raca]["grupos"][grupo] = {
                    "caracteristicas": caracteristicas,
                    "recomendacao_generica": rec_gen.strip(),
                    "especies": {}
                }
            arvore[raca]["grupos"][grupo]["especies"][especie] = {
                "nome_popular": nome_pop.strip(),
                "recomendacao": rec_esp.strip()
            }
    return arvore

def imprimir_arvore(arvore):
    for raca, dados_raca in arvore.items():
        print(f"Raça: {raca}")
        for grupo, dados_grupo in dados_raca["grupos"].items():
            print(f"  Grupo: {grupo}")
            print(f"    Características: {', '.join(dados_grupo['caracteristicas'])}")
            print(f"    Recomendação Genérica: {dados_grupo['recomendacao_generica']}")
            for especie, dados_especie in dados_grupo["especies"].items():
                print(f"      Espécie: {especie} ({dados_especie['nome_popular']})")
                print(f"        Recomendação Específica: {dados_especie['recomendacao']}")

def tratandoEntradaEsp(especieAnimal):
    nomeEspecie = ''
    
    if '-' in especieAnimal:
        temp = especieAnimal.split('-')
        temp = temp[0].capitalize() + '-' + temp[1]
        nomeEspecie = temp
        
    elif ' ' in especieAnimal: 
        temp = especieAnimal.split(' ')
        temp = [i.capitalize() for i in temp]
        for i in temp:
             nomeEspecie = temp[0] + ' ' + temp[1]
    else:
        nomeEspecie = especieAnimal.capitalize()
    print(nomeEspecie)
    return nomeEspecie
    
def removeAcentuacao(texto):
    texto = texto.lower() 
    texto = unicodedata.normalize('NFD', texto)  # separa acentos das letras
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')  # remove os acentos
    texto = texto.replace('ç', 'c')  # trata cedilha
    texto = texto.strip()
    return texto


def recomendar_ambiente(arvore = criar_arvore(CAMINHO_AMBIENTE)):

    raca = str(input("Digite a raça do seu pet (ex: Cachorro, Gato, Lagarto): ")).strip().capitalize()
    especie = str(input("Digite a espécie do seu pet (ou pressione Enter se não souber): ")).strip()
    caracteristicas_input = str(input("Digite características físicas do seu pet, separadas por vírgula (ex: ativo, sociável): ")).strip()
    caracteristicas = [c.strip().lower() for c in caracteristicas_input.split(',')]

    # Tratando entrada da espécie
    nomeEspecie = removeAcentuacao(especie)
    nomeEspecie = tratandoEntradaEsp(nomeEspecie)

    if raca not in arvore:
        print("\n Raça não encontrada no sistema. Verifique a ortografia e tente novamente.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        recomendar_ambiente()

    grupos = arvore[raca]["grupos"]
    grupo_encontrado = None

    # Busca por grupo (1º filtro)
    for grupo, dados_grupo in grupos.items():
        if all(c in dados_grupo["caracteristicas"] for c in caracteristicas):
            grupo_encontrado = grupo
            break

    # Mostrar recomendação mais generalizada
    if grupo_encontrado:
        print(f"\nO ambiente ideal para pets do grupo '{grupo_encontrado}':")
        print(grupos[grupo_encontrado]["recomendacao_generica"])
    else:
        print("\nNenhum grupo correspondente foi encontrado com base nas características fornecidas.")
        print("Mas vamos verificar se conseguimos te ajudar com base apenas na espécie informada...\n")
        time.sleep(1)

    # Recomendação específica da espécie (2º filtro)
    especie_encontrada = False
    for grupo, dados_grupo in grupos.items():
        especies = dados_grupo["especies"]
        for nome_cientifico, dados_especie in especies.items():
            if removeAcentuacao(nomeEspecie).lower() == removeAcentuacao(dados_especie["nome_popular"]).lower():
                especie_encontrada = True
                print(f"Para a espécie '{nome_cientifico}' ou ({dados_especie['nome_popular']}) as condições ideais de ambiente seria(m):")
                print(dados_especie["recomendacao"])
                break
        if especie_encontrada:
            break

    # Breakpoint, o parâmetro do usuário foi absurdo !!
    if not especie_encontrada:
        print(" Não podemos gerar condições de ambiente específica para essa espécie.")
        print("Verifique se a grafia está correta (ex: 'Canis lupus' ou 'canis-lupus').")
        print("Se necessário, tente novamente com outra combinação de dados.")

    menuSairOuReinicio(recomendar_ambiente)


