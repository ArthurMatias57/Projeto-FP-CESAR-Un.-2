import os
os.system("cls")
import random 

# Sugestões Personalizadas de brinquedos ideais, alimentos recomendados e exercíios adequados ----> Baseado em: Peso,Idade e Espécie
# random.choice(lista) -----> escolhe um elemento aleatório de uma lista]

mamiferosAlimentacao = ["Ração Adequada com boa quantidade de micronutrientes","Alimentos naturais","Frutas e Vegetais"]
mamiferosAtividades = ["Caminhadas Longas","Corridas Leves","Brincadeiras em parques","Agility","Atividade em ar livre","Escalada","Túnel de exploração"]
mamiferosBrinquedos = ["Mordedores adequados para o seu animal","Brinquedos de puxar","Brinquedos de arremesso","Pelúcias"]

avesAlimentacao = ["Sementes","Frutas","Pequenos Insetos","Ovos","Ração","Pellets"]
avesAtividades = ["Voo em locais Controlados","Poleiros Móveis","Treinamento com reforço Positivo"]
avesBrinquedos = ["Sinos","Cordas","Brinquedos com desafios de abertura"]

repteisAlimentacao = ["Insetos","Vegetais","Ovos","Frutas","Pequenos pedaços de carne"]
repteisAtividades = ["Exploração com Variações de solo","Banho de sol supervisionados","Treinamento para alimentação com alvo","Locais com variação de temperatura para simular o ambiente natural"]
repteisBrinquedo = ["Piscinas rasas","Caixas para escavação","Troncos Móveis","Rampas","Esconderijos","Rochas Aquecidas"]

peixesAlimentacao = ["Ração específica","Artêmias","Dáfnias","Algas","Pequenos Crustáceos"]
peixesAtividades = ["Correntezas suaves","Obstáculos","Alimentação direcionada com Obstáculos","Iluminação Dinâmica","Esconderijos"]
peixesBrinquedos = ["Plantas Móveis","Cavernas","Estruturas Grandes Submersas","Tubos","Labirintos"]

anfibiosAlimentacao = ["Insetos","Larvas","Ovos","Frutas","Vegetais","Minhocas"]
anfibiosAtividades = ["Esconderijos Variáveis","Passeios monitorados em ambientes diveros","Simulação de sons ambientes","Troca de Substrato"]
anfibiosBrinquedos =["Pedras e Plantas Artificiais","Riachos artificiais com simulação de ambiente","Lugares com correnteza Suave"]






while True:
    try:
        opcao = int(input("BEM VINDO AO PETSCHOOL, O QUE DESEJA?\n[5] - Sugestões Personalizadas\n"))
    except ValueError:
        os.system("cls")
        print("Digito inválido!")
        continue

    match opcao:

        case 5:
            try:
                tipo = int(input("Qual é a classe do seu animal?\n[1] - Mamífero\n[2] - Ave\n[3] - Réptil\n[4] - Peixe\n[5] - Anfíbio\n"))
                if tipo>5 or tipo<1:
                    print("Digite um número entre [1] e [5]!")
                    continue
                porte = int(input("Qual é o porte do seu animal?\n[1] - Grande\n[2] - Médio\n[3] - Pequeno\n"))
                if porte>3 or porte<1:
                    print("Digite um número entre [1] e [3]")
                match tipo:
                    case 1:
                        print(f"\nSua sugestão personalizada está pronta!\nx---------------------------------------------x\
                            \nAlimentação Sugerida: {random.choice(mamiferosAlimentacao)}\nAtividade Sugerida: {random.choice(mamiferosAtividades)}\
                            \nBrinquedo Sugerido: {random.choice(mamiferosBrinquedos)}\nx---------------------------------------------x")
                    case 2:
                        print(f"\nSua sugestão personalizada está pronta!\nx---------------------------------------------x\
                            \nAlimentação Sugerida: {random.choice(avesAlimentacao)}\nAtividade Sugerida: {random.choice(avesAtividades)}\
                            \nBrinquedo Sugerido: {random.choice(avesBrinquedos)}\nx---------------------------------------------x")
                    case 3:
                        print(f"\nSua sugestão personalizada está pronta!\nx---------------------------------------------x\
                            \nAlimentação Sugerida: {random.choice(repteisAlimentacao)}\nAtividade Sugerida: {random.choice(repteisAtividades)}\
                            \nBrinquedo Sugerido: {random.choice(repteisBrinquedo)}\nx---------------------------------------------x")
                    case 4:
                        print(f"\nSua sugestão personalizada está pronta!\nx---------------------------------------------x\
                            \nAlimentação Sugerida: {random.choice(peixesAlimentacao)}\nAtividade Sugerida: {random.choice(peixesAtividades)}\
                            \nBrinquedo Sugerido: {random.choice(peixesBrinquedos)}\nx---------------------------------------------x")
                    case 5:
                        print(f"\nSua sugestão personalizada está pronta!\nx---------------------------------------------x\
                            \nAlimentação Sugerida: {random.choice(anfibiosAlimentacao)}\nAtividade Sugerida: {random.choice(anfibiosAtividades)}\
                            \nBrinquedo Sugerido: {random.choice(anfibiosBrinquedos)}\nx---------------------------------------------x")
            except ValueError:
                print("Digite um valor numérico!")
                continue


