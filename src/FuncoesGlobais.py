import os
import time

"""
Escopo global

"""

#Transição entre telas
def transicao():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Carregando ", end='', flush=True)
    cor = ["\033[31m", "\033[32m", '\033[33m']

    for i in range(3):
        print(cor[i] + '. ' + "\033[0m", end='', flush=True)  # Força cada ponto aparecer
        time.sleep(0.5)

    time.sleep(0.5)  # Pequena pausa final antes de limpar
    os.system('cls' if os.name == 'nt' else 'clear')


# Função para separar visualmente as seções
def lin():
    print("-" * 60)

# Função unificada para menu de saída ou reinício
def menuSairOuReinicio(funcLoop):
    from Funcoes.MenuPrincipal import main

    while True:
        print("-" * 60)
        escolha = input("O que você deseja fazer agora?\n"
                       "1 - Voltar ao menu principal\n"
                       "2 - Reiniciar funcionalidade\n"
                       "Escolha: ").strip()
        print("-" * 60)
        if escolha == "1":
            transicao()
            main()
        elif escolha == "2":
            transicao()
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
#transicao()