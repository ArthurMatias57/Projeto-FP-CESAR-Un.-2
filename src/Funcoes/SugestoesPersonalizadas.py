import os
import random 
import sys
from datetime import datetime
os.system("cls")

#Importação funções globais
CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "..", "BD", "pets.txt")
sys.path.append("Projeto-FP-CESAR-Un.-2\src\FuncoesGlobais.py")
sys.path.append(os.path.dirname(__file__) + "Projeto-FP-CESAR-Un.-2\src")
from FuncoesGlobais import *

# Lista para armazenar os pets
list_pets = []

# Lista para armazenar os eventos
eventos_pet = []

def calcular_idade_pet(data_nascimento):
    """Calcula a idade do pet em anos a partir da data de nascimento"""
    try:
        # Converter a string de data para objeto datetime
        dia, mes, ano = map(int, data_nascimento.split('/'))
        data_nasc = datetime(ano, int(mes), dia)
        
        # Calcular a diferença de tempo
        hoje = datetime.now()
        diferenca = hoje - data_nasc
        
        # Converter para anos (aproximado)
        anos = diferenca.days // 365
        return anos
    except:
        # Em caso de erro, retorna uma idade padrão
        return 0

def obter_sugestoes_por_especie_e_idade(especie, idade):
    """Retorna sugestões personalizadas com base na espécie e idade do pet"""
    # Sugestões para diferentes tipos de animais
    sugestoes = {
        "Cachorro": {
            "filhote": {
                "alimentacao": ["Ração para filhotes", "Alimentação fracionada 3-4 vezes ao dia", "Petiscos específicos para filhotes"],
                "atividades": ["Brincadeiras curtas e frequentes", "Socialização com outros cães", "Treinamento básico de obediência"],
                "brinquedos": ["Mordedores macios", "Brinquedos de pelúcia", "Bolas pequenas e macias"]
            },
            "adulto": {
                "alimentacao": ["Ração Premium para adultos", "Alimentação 2 vezes ao dia", "Petiscos saudáveis"],
                "atividades": ["Caminhadas diárias", "Corridas", "Agility", "Natação"],
                "brinquedos": ["Bolas", "Cordas", "Brinquedos interativos", "Frisbees"]
            },
            "idoso": {
                "alimentacao": ["Ração para cães seniores", "Suplementos para articulações", "Alimentação controlada"],
                "atividades": ["Caminhadas leves", "Exercícios de baixo impacto", "Massagens"],
                "brinquedos": ["Brinquedos macios", "Quebra-cabeças para estímulo mental", "Tapetes de lamber"]
            }
        },
        "Gato": {
            "filhote": {
                "alimentacao": ["Ração para filhotes de gatos", "Alimentação fracionada 3-4 vezes ao dia", "Leite especial para gatinhos"],
                "atividades": ["Brincadeiras com varinha", "Exploração de ambientes", "Socialização"],
                "brinquedos": ["Bolinhas com guizo", "Ratinhos de pelúcia", "Varinhas com penas"]
            },
            "adulto": {
                "alimentacao": ["Ração Premium para gatos adultos", "Alimentação 2 vezes ao dia", "Petiscos específicos para gatos"],
                "atividades": ["Brincadeiras com laser", "Escaladas", "Caça a brinquedos"],
                "brinquedos": ["Arranhadores", "Túneis", "Brinquedos com catnip", "Torres para escalar"]
            },
            "idoso": {
                "alimentacao": ["Ração para gatos seniores", "Suplementos para pelagem e articulações", "Alimentação úmida"],
                "atividades": ["Brincadeiras leves", "Exposição ao sol", "Massagens suaves"],
                "brinquedos": ["Brinquedos macios", "Camas confortáveis", "Brinquedos térmicos"]
            }
        },
        "Ave": {
            "filhote": {
                "alimentacao": ["Papinha especial para filhotes", "Sementes trituradas", "Frutas macias"],
                "atividades": ["Estimulação com sons suaves", "Contato visual frequente", "Ambiente aquecido"],
                "brinquedos": ["Espelhos pequenos", "Poleiros macios", "Brinquedos coloridos"]
            },
            "adulto": {
                "alimentacao": ["Sementes variadas", "Frutas frescas", "Legumes", "Ração específica"],
                "atividades": ["Voos livres supervisionados", "Banhos", "Treinamento de truques"],
                "brinquedos": ["Escadas", "Balanços", "Espelhos", "Brinquedos sonoros"]
            },
            "idoso": {
                "alimentacao": ["Sementes mais macias", "Frutas e legumes picados", "Suplementos vitamínicos"],
                "atividades": ["Exposição ao sol", "Interação tranquila", "Ambiente estável"],
                "brinquedos": ["Poleiros mais largos e estáveis", "Brinquedos fáceis de manipular"]
            }
        },
        "Peixe": {
            "filhote": {
                "alimentacao": ["Ração em pó para alevinos", "Artêmias recém-eclodidas", "Alimentação frequente em pequenas quantidades"],
                "atividades": ["Ambiente com plantas", "Corrente suave", "Esconderijos"],
                "brinquedos": ["Plantas vivas", "Decorações coloridas", "Túneis pequenos"]
            },
            "adulto": {
                "alimentacao": ["Ração específica para a espécie", "Artêmias", "Dáfnias", "Algas"],
                "atividades": ["Correntezas variadas", "Obstáculos", "Alimentação direcionada"],
                "brinquedos": ["Plantas móveis", "Cavernas", "Estruturas para explorar"]
            },
            "idoso": {
                "alimentacao": ["Alimentação mais frequente em menores quantidades", "Alimentos macios", "Suplementos"],
                "atividades": ["Ambiente calmo", "Iluminação adequada", "Temperatura estável"],
                "brinquedos": ["Plantas densas para descanso", "Esconderijos confortáveis"]
            }
        },
        "Réptil": {
            "filhote": {
                "alimentacao": ["Insetos pequenos", "Vegetais tenros", "Suplementos de cálcio"],
                "atividades": ["Banhos de sol controlados", "Ambiente úmido", "Manuseio cuidadoso"],
                "brinquedos": ["Esconderijos pequenos", "Galhos finos", "Substratos variados"]
            },
            "adulto": {
                "alimentacao": ["Insetos vivos", "Vegetais frescos", "Frutas", "Ração específica"],
                "atividades": ["Banhos de sol", "Natação", "Exploração de terrário"],
                "brinquedos": ["Piscinas rasas", "Caixas para escavação", "Troncos"]
            },
            "idoso": {
                "alimentacao": ["Alimentos mais macios", "Suplementação vitamínica", "Hidratação frequente"],
                "atividades": ["Banhos de sol mais longos", "Ambiente com temperatura controlada"],
                "brinquedos": ["Superfícies aquecidas", "Esconderijos confortáveis"]
            }
        }
    }
    
    # Determinar a faixa etária
    if especie.lower() in ["cachorro", "cão"]:
        especie_key = "Cachorro"
        if idade < 2:
            faixa = "filhote"
        elif idade < 7:
            faixa = "adulto"
        else:
            faixa = "idoso"
    elif especie.lower() in ["gato", "felino"]:
        especie_key = "Gato"
        if idade < 1:
            faixa = "filhote"
        elif idade < 10:
            faixa = "adulto"
        else:
            faixa = "idoso"
    elif especie.lower() in ["ave", "pássaro", "passaro", "papagaio", "calopsita"]:
        especie_key = "Ave"
        if idade < 1:
            faixa = "filhote"
        elif idade < 5:
            faixa = "adulto"
        else:
            faixa = "idoso"
    elif especie.lower() in ["peixe", "aquário", "aquario"]:
        especie_key = "Peixe"
        if idade < 1:
            faixa = "filhote"
        elif idade < 3:
            faixa = "adulto"
        else:
            faixa = "idoso"
    elif especie.lower() in ["réptil", "reptil", "lagarto", "tartaruga", "cobra"]:
        especie_key = "Réptil"
        if idade < 1:
            faixa = "filhote"
        elif idade < 5:
            faixa = "adulto"
        else:
            faixa = "idoso"
    else:
        # Espécie não reconhecida, usar sugestões genéricas
        return {
            "alimentacao": ["Ração específica para a espécie", "Consulte um veterinário para recomendações"],
            "atividades": ["Exercícios adequados para a espécie", "Interação diária"],
            "brinquedos": ["Brinquedos apropriados para a espécie", "Enriquecimento ambiental"]
        }
    
    # Retornar sugestões específicas para a espécie e faixa etária
    return sugestoes[especie_key][faixa]

def sugestoesPersonalizadas():
    # Carregar pets para usar informações de espécie e idade
    list_pets.clear()
    carregar_pets(CAMINHO_ARQUIVO, list_pets)
    
    if not list_pets:
        print("Você precisa cadastrar pelo menos um pet antes de receber sugestões personalizadas.")
        print("Por favor, cadastre um pet no menu CRUD primeiro.")
        separar()
        menuSairOuReinicio(obter_sugestoes_por_especie_e_idade)
        return
    
    # Mostrar lista de pets para seleção
    print("Selecione um pet para receber sugestões personalizadas:")
    for i, pet in enumerate(list_pets, 1):
        print(f"{i} - {pet['Nome']} ({pet['Espécie']})")
    
    # Selecionar pet
    while True:
        try:
            escolha = int(input("\nDigite o número do pet: ").strip())
            if 1 <= escolha <= len(list_pets):
                pet_selecionado = list_pets[escolha-1]
                break
            else:
                print(f"Por favor, digite um número entre 1 e {len(list_pets)}.")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    # Obter informações do pet
    nome_pet = pet_selecionado['Nome']
    especie = pet_selecionado['Espécie']
    data_nascimento = pet_selecionado['Data de Nascimento']
    
    # Calcular idade do pet
    idade = calcular_idade_pet(data_nascimento)
    
    # Obter sugestões personalizadas
    sugestoes = obter_sugestoes_por_especie_e_idade(especie, idade)
    
    # Exibir sugestões
    print("\n" + "=" * 60)
    print(f"SUGESTÕES PERSONALIZADAS PARA {nome_pet.upper()}")
    print(f"Espécie: {especie} | Idade aproximada: {idade} anos")
    print("=" * 60)
    
    print("\nALIMENTAÇÃO RECOMENDADA:")
    for item in sugestoes["alimentacao"]:
        print(f"- {item}")
    
    print("\nATIVIDADES RECOMENDADAS:")
    for item in sugestoes["atividades"]:
        print(f"- {item}")
    
    print("\nBRINQUEDOS RECOMENDADOS:")
    for item in sugestoes["brinquedos"]:
        print(f"- {item}")
    
    print("\n" + "=" * 60)
    
    # Menu de opções após exibir sugestões
    while True:
        opcao = input("\nO que você deseja fazer agora?\n"
                     "1 - Ver sugestões para outro pet\n"
                     "2 - Voltar ao menu principal\n"
                     "3 - Sair\n"
                     "Escolha: ").strip()
        
        if opcao == "1":
            return sugestoesPersonalizadas()  # Recursão para mostrar sugestões para outro pet
        elif opcao == "2":
            return  # Volta ao menu principal
        elif opcao == "3":
            print("Encerrando o programa. Até logo!")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")
