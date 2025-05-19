import os
import re
import sys
from datetime import datetime

# Caminho do arquivo
CAMINHO_EVENTOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "BD", "eventos.txt")

#Importação funções global
sys.path.append("Projeto-FP-CESAR-Un.-2\src")
from FuncoesGlobais import *

# Função separadora
def separar():
    print("-" * 60)

# Lista para armazenar os eventos 
eventos_pet = []


def validar_data(data):
    """Valida se a data está no formato DD/MM/AAAA e é uma data válida"""
    # Verificar o formato
    if not re.match(r"^\d{1,2}/\d{1,2}/\d{4}$", data):
        return False
    
    try:
        # Tentar converter para objeto datetime
        dia, mes, ano = map(int, data.split('/'))
        datetime(ano, mes, dia)
        return True
    except ValueError:
        return False

def salvar_eventos():
    # Garantir que o diretório existe
    os.makedirs(os.path.dirname(CAMINHO_EVENTOS), exist_ok=True)
    
    try:
        with open(CAMINHO_EVENTOS, "w", encoding="utf-8") as file:
            for evento in eventos_pet:
                for k, v in evento.items():
                    file.write(f"{k}: {v}\n")
                file.write("-" * 40 + "\n")
        print("Eventos salvos no arquivo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar eventos: {e}")
    separar()

def carregar_eventos():
    # Limpar a lista antes de carregar
    eventos_pet.clear()
    
    try:
        # Verificar se o arquivo existe
        if not os.path.exists(CAMINHO_EVENTOS):
            print("Nenhum arquivo de eventos encontrado. Começando com uma lista vazia.")
            separar()
            return
            
        with open(CAMINHO_EVENTOS, "r", encoding="utf-8") as file:
            evento = {}
            for line in file:
                line = line.strip()
                if line == "-" * 40:
                    if evento:
                        eventos_pet.append(evento)
                        evento = {}
                elif ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    evento[key] = value
            if evento:
                eventos_pet.append(evento)
                
        print(f"{len(eventos_pet)} eventos carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar eventos: {e}")
    separar()

def listar_eventos():
    """Lista todos os eventos cadastrados"""
    if not eventos_pet:
        print("Não há eventos cadastrados.")
        separar()
        return
        
    print("\nLista de eventos cadastrados:")
    separar()
    
    for i, evento in enumerate(eventos_pet, 1):
        print(f"Evento {i}:")
        for chave, valor in evento.items():
            print(f"{chave}: {valor}")
        separar()

def buscar_eventos_por_pet():
    """Busca eventos por nome do pet"""
    if not eventos_pet:
        print("Não há eventos cadastrados.")
        separar()
        return
        
    nome_pet = input("Digite o nome do pet para buscar eventos: ").strip().capitalize()
    separar()
    
    eventos_encontrados = [e for e in eventos_pet if e["Nome do pet"].lower() == nome_pet.lower()]
    
    if not eventos_encontrados:
        print(f"Nenhum evento encontrado para o pet '{nome_pet}'.")
    else:
        print(f"Eventos encontrados para '{nome_pet}':")
        for evento in eventos_encontrados:
            for chave, valor in evento.items():
                print(f"{chave}: {valor}")
            separar()

def excluir_evento():
    """Exclui um evento da lista"""
    if not eventos_pet:
        print("Não há eventos cadastrados para excluir.")
        separar()
        return
        
    listar_eventos()
    
    try:
        indice = int(input("Digite o número do evento que deseja excluir: ")) - 1
        
        if 0 <= indice < len(eventos_pet):
            evento = eventos_pet[indice]
            confirmacao = input(f"Tem certeza que deseja excluir o evento de {evento['Tipo do evento']} para {evento['Nome do pet']}? (s/n): ").lower()
            
            if confirmacao == 's':
                eventos_pet.pop(indice)
                salvar_eventos()
                print("Evento excluído com sucesso!")
            else:
                print("Operação cancelada.")
        else:
            print("Índice inválido!")
    except ValueError:
        print("Por favor, digite um número válido.")
    
    separar()

def registrar_evento():
    # Carregar eventos existentes
    carregar_eventos()
    separar()
    print("Vamos registrar um novo evento para o seu PET!")

    # Validação do nome do pet
    while True:
        nome = input("Nome do pet: ").strip()
        if nome:
            nome = nome.capitalize()
            break
        else:
            print("O nome do pet não pode estar vazio. Tente novamente.")
    separar()

    # Menu de tipos de evento
    print("Qual tipo de evento deseja registrar?")
    print("1 - Vacinação")
    print("2 - Consulta veterinária")
    print("3 - Aplicação de remédio")
    
    # Validação do tipo de evento
    while True:
        tipo = input("Digite o número correspondente: ").strip()
        
        if tipo == "1":
            tipo_evento = "Vacinação"
            break
        elif tipo == "2":
            tipo_evento = "Consulta veterinária"
            break
        elif tipo == "3":
            tipo_evento = "Aplicação de remédio"
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 3.")
    
    separar()

    # Validação da data
    while True:
        data = input("Data do evento (DD/MM/AAAA): ").strip()
        if validar_data(data):
            break
        else:
            print("Formato de data inválido. Use o formato DD/MM/AAAA e uma data válida.")
    
    separar()
    
    # Observações (opcional)
    obs = input("Observações (opcional): ").strip()
    if not obs:
        obs = "Nenhuma"
    separar()

    # Criar e adicionar o evento
    evento = {
        "Nome do pet": nome,
        "Tipo do evento": tipo_evento,
        "Data": data,
        "Observações": obs,
        "Data de registro": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    eventos_pet.append(evento)
    salvar_eventos()
    print("Evento registrado com sucesso!")
    separar()
    
    # Menu de opções após o registro
    while True:
        print("O que deseja fazer agora?")
        print("1 - Registrar outro evento")
        print("2 - Listar todos os eventos")
        print("3 - Buscar eventos por pet")
        print("4 - Excluir um evento")
        print("5 - Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ").strip()
        separar()
        
        if opcao == "1":
            return registrar_evento()  # Recursão para registrar outro evento
        elif opcao == "2":
            listar_eventos()
        elif opcao == "3":
            buscar_eventos_por_pet()
        elif opcao == "4":
            excluir_evento()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")
    
    menuSairOuReinicio(registrar_evento)