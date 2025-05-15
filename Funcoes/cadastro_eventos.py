# Função separadora
def separar():
    print("-" * 60)

# Lista para armazenar os eventos
eventos_pet = []

# Função para registrar eventos 
def registrar_evento():
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
        return

    data = input("Data do evento (DD/MM/AAAA): ").strip()
    separar()
    
    # Verifica se o usuário não inseriu observações
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
    print("Evento registrado com sucesso!")
    separar()

registrar_evento()

# Exibir os eventos registrados 
print("Eventos registrados:")
for evento in eventos_pet:
    print(f"Nome do pet: {evento['Nome do pet']}")
    print(f"Tipo do evento: {evento['Tipo do evento']}")
    print(f"Data: {evento['Data']}")
    print(f"Observações: {evento['Observações']}")
    separar()
