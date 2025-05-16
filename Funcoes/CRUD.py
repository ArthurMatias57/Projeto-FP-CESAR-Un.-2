from BD import pets

def lin():
    print("-" * 60)


list_pets = []

def salvar_pets():
    with open("pets.txt", "a", encoding="utf-8") as file:
        for pet in list_pets:
            for k, v in pet.items():
                file.write(f"{k}: {v}\n")
            file.write("-" * 40 + "\n")  
    print("Dados salvos no arquivo com sucesso!")
    lin()

def carregar_pets():
    try:
        with open("pets.txt", "r", encoding="utf-8") as file:
            pet = {}
            for line in file:
                line = line.strip()
                if line == "-" * 40:
                    if pet:
                        list_pets.append(pet)
                        pet = {}
                elif ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    if key.lower() == "peso":
                        try:
                            value = float(value.replace(",", "."))
                        except ValueError:
                            value = 0.0
                    pet[key] = value
            if pet:
                list_pets.append(pet)
    except FileNotFoundError:
        print("Nenhum arquivo encontrado. Começando com uma lista vazia.")
        lin()
    except Exception as error:
        print(f"Erro ao carregar os pets: {error}")
        lin()

def inicio():
    while True:
        lin()
        final = input("O que você deseja fazer agora?\n"
                      "1 - Voltar ao menu principal\n"
                      "2 - Sair\n"
                      "\nEscolha: ").strip().lower()
        lin()

        if final in ["1", "voltar", "inicio", "menu"]:
            return
        elif final in ["2", "fechar", "sair"]:
            print("Obrigado por usar o Gerenciador de Pets! Até mais.")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

def informacoes():
    while True:
        try:
            name = input("Informe, por favor, o nome do seu pet: ").strip().capitalize()
            if not name.replace(" ", "").isalpha():
                raise ValueError("O nome deve conter apenas letras.")
            lin()
            break
        except ValueError as error:
            print(f"Acho que você errou: {error}")
            lin()

    while True:
        try:
            species = input("Qual é a espécie do seu pet? ").strip().capitalize()
            if not species.replace(" ", "").isalpha():
                raise ValueError("A espécie deve conter apenas letras.")
            lin()
            break
        except ValueError as error:
            print(f"Opa! Parece que houve um erro: {error}")
            lin()

    while True:
        try:
            race = input("E qual é a raça do seu pet? ").strip().capitalize()
            if not race.replace(" ", "").isalpha():
                raise ValueError("A raça deve conter apenas letras.")
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
        except ValueError:
            print("Erro: Insira um número válido para o dia.")
            lin()

    mounths = {
        "janeiro": ["janeiro", "01", "1"], "fevereiro": ["fevereiro", "02", "2"], "março": ["março", "marco", "03", "3"],
        "abril": ["abril", "04", "4"], "maio": ["maio", "05", "5"], "junho": ["junho", "06", "6"], "julho": ["julho", "07", "7"],
        "agosto": ["agosto", "08", "8"], "setembro": ["setembro", "09", "9"], "outubro": ["outubro", "10"],
        "novembro": ["novembro", "11"], "dezembro": ["dezembro", "12"]
    }

    while True:
        mounth = input("Digite o mês de nascimento (nome ou número): ").strip().lower()
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

    while True:
        try:
            year = int(input("Digite o ano de nascimento (ex: 2020): "))
            if year < 1900 or year > 2025:
                raise ValueError("Ano inválido!")
            lin()
            break
        except ValueError:
            print("Erro: Insira um número válido para o ano.")
            lin()

    date_birth = f"{day}/{mounth}/{year}"

    while True:
        try:
            weight = float(input("Informe o peso do seu pet (em kg): ").strip().replace(",", "."))
            if weight <= 0:
                raise ValueError("Peso inválido.")
            lin()
            break
        except ValueError as error:
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
    inicio()

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
    inicio()

def edit():
    if list_pets:
        for ordem, pet in enumerate(list_pets):
            print(f"Pet {ordem + 1} - {pet['Nome']}")
            lin()

        while True:
            try:
                number = int(input("\nDigite o número do pet que deseja alterar: ")) - 1
                if number < 0 or number >= len(list_pets):
                    raise IndexError("Número fora da lista.")
                lin()
                break
            except ValueError:
                print("Erro: Insira um número válido.")
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
                list_pets[number]["Nome"] = input("Digite o novo nome do seu pet: ").strip().title()
                break
            elif item in ['2', "espécie", "especie"]:
                list_pets[number]["Espécie"] = input("Digite a nova espécie: ").strip().capitalize()
                break
            elif item in ['3', "raça", "raca"]:
                list_pets[number]["Raça"] = input("Digite a nova raça: ").strip().capitalize()
                break
            elif item in ['4', "peso", "massa"]:
                while True:
                    try:
                        novo_peso = float(input("Digite o novo peso: ").replace(",", ".").strip())
                        if novo_peso <= 0:
                            raise ValueError("Peso deve ser um número positivo.")
                        list_pets[number]["Peso"] = novo_peso
                        break
                    except ValueError as error:
                        print(f"Tente novamente! {error}")
                        lin()
            else:
                print("Opção inválida!")
                lin()
                continue

        salvar_pets()
        print("Alteração realizada com sucesso!")
        lin()
    else:
        print("Nenhum pet cadastrado.")
        lin()

    inicio()

def remove():
    if list_pets:
        for ordem, pet in enumerate(list_pets):
            print(f"Pet {ordem + 1} - {pet['Nome']}")
            lin()

        while True:
            try:
                number = int(input("\nDigite o número do pet que deseja remover: ")) - 1
                if number < 0 or number >= len(list_pets):
                    raise IndexError("Número fora da lista.")
                lin()
                break
            except ValueError:
                print("Erro: Insira um número válido.")
                lin()
            except IndexError as error:
                print(f"Tente novamente! {error}")
                lin()

        list_pets.pop(number)
        salvar_pets()
        print("Pet removido com sucesso!")
        lin()
    else:
        print("Nenhum pet cadastrado.")
        lin()

    inicio()

carregar_pets()

def CRUD():
    while True:
        lin()
        escolha = input("Selecione uma opção:\n"
                        "\n1 - Cadastrar pet\n"
                        "2 - Visualizar pets cadastrados\n"
                        "3 - Editar pet\n"
                        "4 - Remover pet\n"
                        "5 - Sair\n"
                        "\nQual a sua decisão: ").strip().lower()
        lin()

        if escolha in ['1', "cadastrar", "adicionar"]:
            informacoes()
        elif escolha in ['2', "visualizar", "lista", "ler"]:
            read()
        elif escolha in ['3', "editar", "alterar", "mudar"]:
            edit()
        elif escolha in ['4', "remover", "excluir", "deletar"]:
            remove()
        elif escolha in ['5', "sair", "exit", "fechar"]:
            print("Obrigado por usar o Gerenciador de Pets! Até mais.")
            break
        else:
            print("Opção inválida! Escolha um número correto.")
            lin()
            