import os


"""
Escopo global

"""


# Função para separar visualmente as seções
def lin():
    print("-" * 60)

def separar():
    print("-" * 60)

def template():
    print("-" * 60)

# Função unificada para menu de saída ou reinício
def menuSairOuReinicio(funcLoop):
    from Inicio import inicio
    
    while True:
        print("-" * 60)
        escolha = input("O que você deseja fazer agora?\n"
                       "1 - Voltar ao menu principal\n"
                       "2 - Reiniciar funcionalidade\n"
                       "Escolha: ").strip()
        print("-" * 60)
        if escolha == "1":
            inicio()
        elif escolha == "2":
            funcLoop()
        else:
            print("Opção inválida. Tente novamente.")


"""
Para uso em CRUD e sugestões personalizadas

"""

def carregar_pets(CAMINHO_PETS, list_pets):
    try:
        # Verificar se o arquivo existe
        if not os.path.exists(CAMINHO_PETS):
            print("Nenhum arquivo encontrado. Começando com uma lista vazia.")
            lin()
            return
            
        with open(CAMINHO_PETS, "r", encoding="utf-8") as file:
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
        
        print(f"{len(list_pets)} pets carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
    lin()
