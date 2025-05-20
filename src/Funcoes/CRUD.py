import os
import sys
import random
import re
from datetime import datetime

CAMINHO_PETS = os.path.join("Projeto-FP-CESAR-Un.-2\src\BD\pets.txt")

#Importação funções globais
sys.path.append("Projeto-FP-CESAR-Un.-2\src")
from FuncoesGlobais import *

list_pets = []

def salvar_pets():
    # Garantir que o diretório existe
    os.makedirs(os.path.dirname(CAMINHO_PETS), exist_ok=True)
    
    try:
        with open(CAMINHO_PETS, "w", encoding="utf-8") as file:
            for pet in list_pets:
                for k, v in pet.items():
                    file.write(f"{k}: {v}\n")
                file.write("-" * 40 + "\n")  
        print("Dados salvos no arquivo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
    lin()


def informacoes():
    while True:
        try:
            name = input("Informe, por favor, o nome do seu pet: ").strip()
            if not name:
                raise ValueError("O nome não pode estar vazio.")
            if not name.replace(" ", "").isalpha():
                raise ValueError("O nome deve conter apenas letras.")
            name = name.capitalize()
            lin()
            break
        except ValueError as error:
            print(f"Acho que você errou: {error}")
            lin()

    while True:
        try:
            species = input("Qual é a espécie do seu pet? ").strip()
            if not species:
                raise ValueError("A espécie não pode estar vazia.")
            if not species.replace(" ", "").isalpha():
                raise ValueError("A espécie deve conter apenas letras.")
            species = species.capitalize()
            lin()
            break
        except ValueError as error:
            print(f"Opa! Parece que houve um erro: {error}")
            lin()

    while True:
        try:
            race = input("E qual é a raça do seu pet? ").strip()
            if not race:
                raise ValueError("A raça não pode estar vazia.")
            if not race.replace(" ", "").isalpha():
                raise ValueError("A raça deve conter apenas letras.")
            race = race.capitalize()
            lin()
            break
        except ValueError as error:
            print(f"Acho que você se enganou: {error}")
            lin()

    print("\nInforme a data de nascimento do seu pet:\n")

    while True:
        try:
            day = int(input("Digite o dia de nascimento (1-31): "))
            if day < 1 or day > 31:
                raise ValueError("O dia deve estar entre 1 e 31.")
            lin()
            break
        except ValueError as e:
            if "invalid literal for int" in str(e):
                print("Erro: Insira um número válido para o dia.")
            else:
                print(f"Erro: {e}")
            lin()

    mounths = {
        "janeiro": ["janeiro", "01", "1"], "fevereiro": ["fevereiro", "02", "2"], "março": ["março", "marco", "03", "3"],
        "abril": ["abril", "04", "4"], "maio": ["maio", "05", "5"], "junho": ["junho", "06", "6"], "julho": ["julho", "07", "7"],
        "agosto": ["agosto", "08", "8"], "setembro": ["setembro", "09", "9"], "outubro": ["outubro", "10"],
        "novembro": ["novembro", "11"], "dezembro": ["dezembro", "12"]
    }

    while True:
        mounth = input("Digite o mês de nascimento (nome ou número): ").strip().lower()
        if not mounth:
            print("O mês não pode estar vazio.")
            continue
            
        found = False
        for key, value in mounths.items():  
            if mounth in value:
                mounth = value[1]
                found = True
                break
        if found:
            lin()
            break
        else:
            print("Erro: Mês inválido.")
            lin()

    current_year = datetime.now().year
    while True:
        try:
            year = int(input("Digite o ano de nascimento (ex: 2020): "))
            if year < 1900 or year > current_year:
                raise ValueError(f"Ano inválido! Deve estar entre 1900 e {current_year}.")
            lin()
            break
        except ValueError as e:
            if "invalid literal for int" in str(e):
                print("Erro: Insira um número válido para o ano.")
            else:
                print(f"Erro: {e}")
            lin()

    # Validar a data completa
    try:
        data_nascimento = datetime(year, int(mounth), day)
        if data_nascimento > datetime.now():
            print("Aviso: A data de nascimento é no futuro. Verifique se está correta.")
    except ValueError:
        print("Aviso: A combinação de dia/mês/ano não forma uma data válida. Usando mesmo assim.")
    
    date_birth = f"{day}/{mounth}/{year}"

    while True:
        try:
            weight_input = input("Informe o peso do seu pet (em kg): ").strip().replace(",", ".")
            if not weight_input:
                raise ValueError("O peso não pode estar vazio.")
            weight = float(weight_input)
            if weight <= 0:
                raise ValueError("Peso inválido. Deve ser maior que zero.")
            lin()
            break
        except ValueError as error:
            if "could not convert string to float" in str(error):
                print("Erro: Digite um número válido para o peso.")
            else:
                print(f"Opa! Parece que houve um erro: {error}")
            lin()

    pet = {
        "Nome": name,
        "Espécie": species,
        "Raça": race,
        "Data de Nascimento": date_birth,
        "Peso": weight
    }

    list_pets.append(pet)
    salvar_pets()
    print("Cadastro realizado com sucesso!")
    lin()
    menuSairOuReinicio(CRUD)

def read():
    if list_pets:
        print("\nA lista de pets cadastrados:\n")
        lin()
        for ordem, pet in enumerate(list_pets, 1):
            print(f"Pet {ordem}:")
            lin()
            for key, value in pet.items():
                print(f"{key}: {value}")
            lin()
    else:
        print("Ainda não foi cadastrado nenhum pet.")
    lin()
    menuSairOuReinicio(CRUD)
    

def edit():
    if list_pets:
        for ordem, pet in enumerate(list_pets):
            print(f"Pet {ordem + 1} - {pet['Nome']}")
            lin()

        while True:
            try:
                number_input = input("\nDigite o número do pet que deseja alterar: ").strip()
                if not number_input:
                    raise ValueError("O número não pode estar vazio.")
                number = int(number_input) - 1
                if number < 0 or number >= len(list_pets):
                    raise IndexError("Número fora da lista.")
                lin()
                break
            except ValueError as e:
                if "invalid literal for int" in str(e):
                    print("Erro: Insira um número válido.")
                else:
                    print(f"Erro: {e}")
                lin()
            except IndexError as error:
                print(f"Tente novamente! {error}")
                lin()

        while True:
            item = input("\nQual item deseja editar?\n"
                         "1 - Nome\n"
                         "2 - Espécie\n"
                         "3 - Raça\n"
                         "4 - Peso\n"
                         "\nSua escolha: ").strip().lower()
            lin()

            if item in ['1', "nome"]:
                while True:
                    novo_nome = input("Digite o novo nome do seu pet: ").strip()
                    if not novo_nome:
                        print("O nome não pode estar vazio.")
                        continue
                    if not novo_nome.replace(" ", "").isalpha():
                        print("O nome deve conter apenas letras.")
                        continue
                    list_pets[number]["Nome"] = novo_nome.title()
                    break
                break
            elif item in ['2', "espécie", "especie"]:
                while True:
                    nova_especie = input("Digite a nova espécie: ").strip()
                    if not nova_especie:
                        print("A espécie não pode estar vazia.")
                        continue
                    if not nova_especie.replace(" ", "").isalpha():
                        print("A espécie deve conter apenas letras.")
                        continue
                    list_pets[number]["Espécie"] = nova_especie.capitalize()
                    break
                break
            elif item in ['3', "raça", "raca"]:
                while True:
                    nova_raca = input("Digite a nova raça: ").strip()
                    if not nova_raca:
                        print("A raça não pode estar vazia.")
                        continue
                    if not nova_raca.replace(" ", "").isalpha():
                        print("A raça deve conter apenas letras.")
                        continue
                    list_pets[number]["Raça"] = nova_raca.capitalize()
                    break
                break
            elif item in ['4', "peso", "massa"]:
                while True:
                    try:
                        peso_input = input("Digite o novo peso: ").replace(",", ".").strip()
                        if not peso_input:
                            raise ValueError("O peso não pode estar vazio.")
                        novo_peso = float(peso_input)
                        if novo_peso <= 0:
                            raise ValueError("Peso deve ser um número positivo.")
                        list_pets[number]["Peso"] = novo_peso
                        break
                    except ValueError as error:
                        if "could not convert string to float" in str(error):
                            print("Erro: Digite um número válido para o peso.")
                        else:
                            print(f"Tente novamente! {error}")
                        lin()
                break
            else:
                print("Opção inválida, tente novamente.")
                lin()

        salvar_pets()
        print("Informações atualizadas com sucesso!")
    else:
        print("Nenhum pet cadastrado para editar.")
    lin()
    menuSairOuReinicio(CRUD)
    

def remove():
    if list_pets:
        for ordem, pet in enumerate(list_pets):
            print(f"Pet {ordem + 1} - {pet['Nome']}")
            lin()
        while True:
            try:
                escolha_input = input("Digite o número do pet que deseja remover: ").strip()
                if not escolha_input:
                    raise ValueError("O número não pode estar vazio.")
                escolha = int(escolha_input) - 1
                if escolha < 0 or escolha >= len(list_pets):
                    raise IndexError("Número fora da lista.")
                lin()
                break
            except ValueError as e:
                if "invalid literal for int" in str(e):
                    print("Digite um número válido.")
                else:
                    print(f"Erro: {e}")
                lin()
            except IndexError as error:
                print(f"Tente novamente! {error}")
                lin()
        confirm = input(f"Tem certeza que deseja remover {list_pets[escolha]['Nome']}? (s/n): ").lower()
        if confirm == "s":
            del list_pets[escolha]
            salvar_pets()
            print("Pet removido com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("Nenhum pet cadastrado para remover.")
    lin()
    menuSairOuReinicio(CRUD)
    

def CRUD():
    # Limpar a lista antes de carregar
    list_pets.clear()
    carregar_pets(CAMINHO_PETS, list_pets)
    
    while True:
        print("\nO que você deseja fazer?")
        print("1 - Cadastrar novo pet")
        print("2 - Ver pets cadastrados")
        print("3 - Editar informações de pet")
        print("4 - Remover pet")
        print("5 - Voltar ao menu principal")
        
        opcao = input("\nEscolha uma opção: ").strip()
        lin()
        
        if opcao == "1":
            informacoes()
            return
        elif opcao == "2":
            read()
            return
        elif opcao == "3":
            edit()
            return
        elif opcao == "4":
            remove()
            return
        elif opcao == "5":
            return
        else:
            print("Opção inválida. Tente novamente.")

#CRUD()