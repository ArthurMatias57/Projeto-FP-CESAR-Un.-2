import os

# Caminho do arquivo
CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "..", "BD", "eventos_pet.txt")

# Função separadora
def separar():
    print("-" * 60)

# Lista para armazenar os eventos 
eventos_pet = []

# Função para registrar eventos
def registrar_evento():
    while True:
        try:
            separar()
            print("Vamos registrar um novo evento para o seu PET!")

            nome = input("Nome do pet: ").strip().capitalize()
            separar()

            print("Qual tipo de evento deseja registrar?")
            print("1 - Vacinação")
            print("2 - Consulta veterinária")
            print("3 - Aplicação de remédio")
            tipo = input("Digite o número correspondente: ").strip()
            separar()

            if tipo == "1":
                tipo_evento = "Vacinação"
            elif tipo == "2":
                tipo_evento = "Consulta veterinária"
            elif tipo == "3":
                tipo_evento = "Aplicação de remédio"
            else:
                print("Tipo inválido. O evento não foi registrado.")
                separar()
                continue

            data = input("Data do evento (DD/MM/AAAA): ").strip()
            separar()

            obs = input("Observações (opcional): ").strip()
            if not obs:
                obs = "Nenhuma"
            separar()

            evento = {
                "Nome do pet": nome,
                "Tipo do evento": tipo_evento,
                "Data": data,
                "Observações": obs
            }

            eventos_pet.append(evento)

            # Salva o evento no arquivo
            with open(CAMINHO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
                arquivo.write(f"{nome}|{tipo_evento}|{data}|{obs}\n")

            print("Evento registrado com sucesso!")
            separar()

            print("Eventos registrados até agora:")
            try:
                with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                    for linha in arquivo:
                        partes = linha.strip().split('|')
                        if len(partes) == 4:
                            print(f"Nome do pet: {partes[0]}")
                            print(f"Tipo do evento: {partes[1]}")
                            print(f"Data: {partes[2]}")
                            print(f"Observações: {partes[3]}")
                            separar()
            except FileNotFoundError:
                print("Nenhum evento registrado ainda.")

            opcao = input("Deseja registrar mais algum evento? (sim/nao): ").strip().lower()
            if opcao != "sim":
                break

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            print("Tente novamente.")
            continue

    print("Retornando ao menu principal...")
    CRUD()  

