# Função para imprimir uma linha separadora
def lin():
    print("-" * 60)

# 1. CRUD de Animais de Estimação:
# Camila poderá adicionar, visualizar, editar e excluir registros dos seus pets,
# com essas informações: nome, espécie, raça, data de nascimento e peso.

# Define a função 'informacoes' que irá coletar os dados do novo pet.
def informacoes(listaDePets):

        # Solicita o nome do pet, remove espaços em branco e capitaliza a primeira letra.
        name = input("Informe, por favor, o nome do seu pet: ").strip().capitalize()
        lin()

        while not name.replace(" ", "").isalpha(): #Remove espaços TEMPORARIAMENTE (replace("", "")) para verificar se o nome contém apenas STRINGS(isalpha())
            
            print("Acho que você errou, o nome deve contar apenas letras.")
            lin()
            name = input("Informe, novamente, o nome do seu pet: ").strip().capitalize()
            lin()

        # Solicita a espécie do pet, trata o texto da mesma forma.
        especie = input("Qual é a espécie do seu pet? ").strip().capitalize()
        lin()

        # Solicita a raça do pet.
        raca = input("E qual é a raça? ").strip().capitalize()
        lin()

        # Solicita a data de nascimento do pet no formato DD/MM/AAAA.
        date_nasc = input("Qual é a data de nascimento do seu pet? (DD/MM/AAAA): ").strip()
        lin()

        # Solicita o peso do pet, tratando espaços em branco.
        peso = input("Gentilmente, informe o peso do seu pet (em kg): ").strip().replace(",", ".") #
        lin()

        # Enquanto o peso estiver vazio ou for menor/igual a zero, continua pedindo um valor válido.
        while peso == "" or not peso.replace(".", "", 1) or float(peso) <= 0:              # peso.replace(".", "", 1) -> 
            if peso == float(peso) <= 0:
                # Informa ao usuário que o valor está incorreto.
                print("Opa! Parece que houve um erro. O peso deve ser um número positivo.")
                lin()
            elif peso == "":
                print("Você esqueceu do peso de seu pet. Tente novamente!")
                # Pede ao usuário que tente novamente.
                peso = input("Tente novamente, por favor: qual é o peso do seu pet (em kg)? ").strip()
        
        peso = float(peso)
        lin()

        # Cria um dicionário com todas as informações do pet.
        pets = {
            "Nome: ": name,
            "Espécie: ": especie,
            "Raça: ": raca,
            "Data de nascimento: ": date_nasc,
            "Peso: ": peso
        }

        # Adiciona o dicionário do pet à lista de pets.
        listaDePets.append(pets)

        # Informa ao usuário que o cadastro foi realizado com sucesso.
        print("Muito bem! O cadastro do seu pet foi realizado com sucesso.")
        lin()


def CRUD():
    # Solicita ao usuário que escolha uma das opções do menu do CRUD de pets, com uma mensagem respeitosa.
    lin()
    escolha = ""
    while escolha not in ['1', "cadastrar", "adicionar"]:

        escolha = input("Por gentileza, selecione a opção desejada no seu Gerenciador de Pets:\n" \
                            "\n1 - Cadastrar um novo pet\n" \
                            "2 - Visualizar pets cadastrados\n" \
                            "3 - Atualizar informações de um pet\n" \
                            "4 - Remover um pet da lista\n" \
                            "\nQual foi a sua decisão: ").strip().lower()
        lin()

        # Cria uma lista vazia onde serão armazenados os pets cadastrados como dicionários.
        list_pets = []

        # Verifica se a opção escolhida foi "1 - Cadastrar um novo pet".

        if escolha in ['1', "cadastrar", "adicionar"]: 
            # Chama a função informacoes para executar o processo de cadastro.
            informacoes(list_pets)

        elif escolha == "":
            print("Eita! Você esqueceu de escolher a sua opção. Tente novamente!")

        else:
            print("Ops, tente novamente, escolha uma opção disponível!")

    if escolha == 2:

        def read():
            for i in list_pets:
                print(i)
        read()
CRUD()

# 2. Cadastro de Cuidados e Eventos:
# O sistema permitirá o registro de eventos importantes, sendo eles: vacinações,
# consultas veterinárias e aplicação de remédios. Para cada evento deve ser
# registrado datas, o nome do pet e observações.

# Define a função eventos() que será responsável por registrar eventos relacionados ao PET.
def eventos():
    
    # Chama a função lin(), provavelmente usada para imprimir uma linha separadora (por exemplo, '------').
    lin()
    
    # Solicita ao usuário que escolha o tipo de evento a ser registrado e converte a resposta para inteiro.
    opcao = int(input("Por favor, escolha o tipo de evento que você deseja registrar:\n"
                      "1 - Vacinação\n"
                      "2 - Consultas Veterinárias\n"
                      "3 - Aplicação de remédios\n"))
    
    # Chama novamente a função lin() para separar visualmente a próxima parte do código.
    lin()
    
    # Verifica se a opção digitada não está entre as válidas (1, 2 ou 3).
    if opcao not in [1, 2, 3]:
        # Informa que a opção escolhida é inválida.
        print("Desculpe, essa opção não é válida. Por favor, escolha entre as opções disponíveis!")
        lin()
        # Encerra a função sem executar o restante do código.
        return
    
    # Se a opção escolhida foi 1 (Vacinação):
    if opcao == 1:
        # Inicializa contador de vacinações.
        cont_vac = 0
        # Cria uma lista para armazenar datas de vacinações registradas.
        list_date_vac = []

        # Pergunta ao usuário se o pet recebeu vacinação recentemente.
        vac = input("Seu PET recebeu alguma vacinação recentemente? Responda com 'Sim' ou 'Não': ").strip().lower()
        lin()
        
        # Se a resposta for "sim", registra a vacinação.
        if vac == "sim":
            # Incrementa o contador de vacinações.
            cont_vac += 1
            # Solicita a data da última vacinação.
            date_vac = input("Qual foi a data da última vacinação do seu PET? Por favor, insira a data no formato DD/MM/AAAA: ").strip()
            lin()
            
            # Verifica se a data ainda não está na lista de vacinações.
            if date_vac not in list_date_vac:
                # Adiciona a nova data à lista.
                list_date_vac.append(date_vac)
                # Confirma o registro do evento.
                print("Muito obrigado! O evento de vacinação foi registrado com sucesso.")
                lin()
            else:
                # Informa que a data já está cadastrada.
                print("A data informada já está registrada. Não é necessário adicionar novamente.")
                lin()
    
    # Se a opção escolhida foi 2 (Consulta veterinária):
    elif opcao == 2:
        # Inicializa contador de consultas.
        cont_cons_vet = 0
        # Cria lista para armazenar datas de consultas veterinárias.
        list_date_cons_vet = []

        # Pergunta ao usuário se houve consulta recentemente.
        cons_vet = input("Seu PET teve consulta veterinária recentemente? Responda com 'Sim' ou 'Não': ").strip().lower()
        lin()
        
        # Se a resposta for "sim", registra a consulta.
        if cons_vet == "sim":
            # Incrementa o contador.
            cont_cons_vet += 1
            # Solicita a data da consulta.
            date_cons = input("Por favor, informe a data da última consulta veterinária do seu PET no formato DD/MM/AAAA: ").strip()
            lin()
            
            # Verifica se a data ainda não foi registrada.
            if date_cons not in list_date_cons_vet:
                # Adiciona a data à lista.
                list_date_cons_vet.append(date_cons)
                # Confirma o registro.
                print("Muito obrigado! O evento de consulta foi registrado com sucesso.")
                lin()
            else:
                # Informa que a data já está cadastrada.
                print("A data informada já está registrada. Não é necessário adicionar novamente.")
                lin()
    
    # Se a opção escolhida foi 3 (Aplicação de remédio):
    elif opcao == 3:
        # Inicializa contador de medicações.
        cont_rem = 0
        # Lista para nomes dos remédios registrados.
        list_rem = []
        # Lista para datas em que o remédio foi administrado.
        list_date_rem = []

        # Pergunta ao usuário se o pet precisou de medicação.
        rem = input("O seu PET precisou de alguma medicação recentemente? Responda com 'Sim' ou 'Não': ").strip().lower()
        lin()
        
        # Se sim, registra o evento.
        if rem == "sim":
            # Incrementa o contador.
            cont_rem += 1
            # Pede o nome do remédio.
            esp_rem = input("Por favor, informe o nome da medicação administrada ao seu PET: ").strip()
            lin()
            
            # Se o nome do remédio ainda não estiver na lista, adiciona.
            if esp_rem not in list_rem:
                list_rem.append(esp_rem)
            
            # Solicita a data da administração do remédio.
            date_rem = input("Qual foi a data da administração dessa medicação? Por favor, insira no formato DD/MM/AAAA: ").strip()
            lin()
            
            # Verifica se a data ainda não foi registrada.
            if date_rem not in list_date_rem:
                # Adiciona à lista.
                list_date_rem.append(date_rem)
                # Confirma o registro.
                print("Muito obrigado! O evento de aplicação de medicação foi registrado com sucesso.")
                lin()
            else:
                # Informa que a data já está cadastrada.
                print("A data informada já está registrada. Não é necessário adicionar novamente.")
                lin()