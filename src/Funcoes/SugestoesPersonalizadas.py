
import os
os.system("cls")
import random 
from FuncoesGlobais import *

# Sugestões Personalizadas de brinquedos ideais, alimentos recomendados e exercíios adequados ----> Baseado em: Peso,Idade e Espécie
# random.choice(lista) -----> escolhe um elemento aleatório de uma lista]

def SugestoesPersonalizadas():

    mamiferosAlimentacao = ["Ração Adequada com boa quantidade de micronutrientes","Alimentos naturais","Frutas e Vegetais"]
    mamiferosAtividades = ["Caminhadas Longas","Corridas Leves","Brincadeiras em parques","Agility","Atividade em ar livre","Escalada","Túnel de exploração"]
    mamiferosBrinquedos = ["Mordedores adequados para o seu animal","Brinquedos de puxar","Brinquedos de arremesso","Pelúcias"]
    cuidados_mamiferos_jovens = ["Socialização precoce com humanos e outros animais.","Brinquedos apropriados para dentição.","Treinamento básico com reforço positivo."]
    cuidados_mamiferos_adultos = ["Rotina consistente de atividades físicas.","Check-up anual e controle antiparasitário.","Alimentação balanceada para fase adulta."]
    cuidados_mamiferos_idosos = ["Atenção à mobilidade: rampas, piso antiderrapante.","Exames geriátricos frequentes.","Alimentos de fácil digestão e ricos em antioxidantes."]



    avesAlimentacao = ["Sementes","Frutas","Pequenos Insetos","Ovos","Ração","Pellets"]
    avesAtividades = ["Voo em locais Controlados","Poleiros Móveis","Treinamento com reforço Positivo"]
    avesBrinquedos = ["Sinos","Cordas","Brinquedos com desafios de abertura"]
    cuidados_aves_jovens = ["Manipulação cuidadosa e diária.","Alimentação assistida sob orientação veterinária.","Estimulação com brinquedos coloridos e móveis."]
    cuidados_aves_adultos = ["Enriquecimento ambiental rotativo.","Voos supervisionados em ambientes seguros.","Evitar estresse com mudanças bruscas."]
    cuidados_aves_idosos = ["Verificação frequente de bico e unhas.","Poleiros mais grossos e confortáveis.","Dieta equilibrada para evitar carências nutricionais."]


    repteisAlimentacao = ["Insetos","Vegetais","Ovos","Frutas","Pequenos pedaços de carne"]
    repteisAtividades = ["Exploração com Variações de solo","Banho de sol supervisionados","Treinamento para alimentação com alvo","Locais com variação de temperatura para simular o ambiente natural"]
    repteisBrinquedo = ["Piscinas rasas","Caixas para escavação","Troncos Móveis","Rampas","Esconderijos","Rochas Aquecidas"]
    cuidados_repteis_jovens = ["Temperatura e umidade do terrário controladas.","Alimentação frequente em porções menores.","Evitar manipulação excessiva."]
    cuidados_repteis_adultos = ["Controle de crescimento com acompanhamento veterinário.","Revisão da iluminação UVB e fotoperíodo.","Oferecer esconderijos variados."]
    cuidados_repteis_idosos = ["Ajuste na dieta para facilitar digestão.","Monitorar muda da pele com mais atenção.","Evitar manipulação desnecessária."]


    peixesAlimentacao = ["Ração específica","Artêmias","Dáfnias","Algas","Pequenos Crustáceos"]
    peixesAtividades = ["Correntezas suaves","Obstáculos","Alimentação direcionada com Obstáculos","Iluminação Dinâmica","Esconderijos"]
    peixesBrinquedos = ["Plantas Móveis","Cavernas","Estruturas Grandes Submersas","Tubos","Labirintos"]
    cuidados_peixes_jovens = ["Alimentação rica em proteínas em pequenas porções frequentes.","Evitar espécies agressivas.","Manter parâmetros de água muito estáveis."]
    cuidados_peixes_adultos = ["Aquário bem ciclado e filtrado.","Interações com o ambiente (plantas, tocas, espelhos).","Evitar superpopulação no aquário."]
    cuidados_peixes_idosos = ["Luz indireta e fotoperíodo tranquilo.","Alimentos macios e fáceis de ingerir.","Evitar introdução de novos peixes ou realocação."]


    anfibiosAlimentacao = ["Insetos","Larvas","Ovos","Frutas","Vegetais","Minhocas"]
    anfibiosAtividades = ["Esconderijos Variáveis","Passeios monitorados em ambientes diveros","Simulação de sons ambientes","Troca de Substrato"]
    anfibiosBrinquedos =["Pedras e Plantas Artificiais","Riachos artificiais com simulação de ambiente","Lugares com correnteza Suave"]
    cuidados_anfibios_jovens = ["Manter pH e temperatura ideais da água.","Evitar correntes de ar e manuseio."]
    cuidados_anfibios_adultos = ["Ambiente bem plantado com esconderijos e obstáculos.","Manutenção rigorosa da qualidade da água.","Evitar estresse com movimentos bruscos."]
    cuidados_anfibios_idosos = ["Monitoramento de sinais de fungos ou infecções.","Redução da frequência alimentar.","Evitar troca de habitat para reduzir estresse."]









    while True:
                try:
                    opcoes = int(input("Qual opção você deseja?\n[1] - Sugestões personalizadas\n[2] - Voltar"))
                    if opcoes == 1:
                        tipo = int(input("Qual é a classe do seu animal?\n[1] - Mamífero\n[2] - Ave\n[3] - Réptil\n[4] - Peixe\n[5] - Anfíbio\nR: "))
                        if tipo>5 or tipo<1:
                            os.system("cls")
                            print("Digite um número entre [1] e [5]!")
                            continue
                        porte = int(input("Qual é o porte do seu animal?\n[1] - Grande\n[2] - Médio\n[3] - Pequeno\nR: "))
                        if porte>3 or porte<1:
                            os.system("cls")
                            print("Digite um número entre [1] e [3]")
                            continue
                        faixa_etaria = int(input("Qual a faixa etária do seu animal?\n[1] - Jovem\n[2] - Adulto\n[3] - Idoso\nR: "))
                        if faixa_etaria>3 or porte<1:
                            os.system("cls")
                            print("Digite um número entre [1] e [3]")
                            continue
                        match tipo:
                            case 1:
                                print(f"\nSua sugestão personalizada está pronta!\nx---------------------------------------------x\
                                    \nAlimentação Sugerida: {random.choice(mamiferosAlimentacao)}\nAtividade Sugerida: {random.choice(mamiferosAtividades)}\
                                    \nBrinquedo Sugerido: {random.choice(mamiferosBrinquedos)}\nx---------------------------------------------x")
                                match faixa_etaria:
                                    case 1:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_mamiferos_jovens)}\nx---------------------------------------------x\n")
                                    case 2:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_mamiferos_adultos)}\nx---------------------------------------------x\n")
                                    case 3:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_mamiferos_idosos)}\nx---------------------------------------------x\n")
                            case 2:
                                print(f"\nSua sugestão personalizada está pronta!\nx---------------------------------------------x\
                                    \nAlimentação Sugerida: {random.choice(avesAlimentacao)}\nAtividade Sugerida: {random.choice(avesAtividades)}\
                                    \nBrinquedo Sugerido: {random.choice(avesBrinquedos)}\nx---------------------------------------------x")
                                match faixa_etaria:
                                    case 1:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_aves_jovens)}\nx---------------------------------------------x\n")
                                    case 2:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_aves_adultos)}\nx---------------------------------------------x\n")
                                    case 3:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_aves_idosos)}\nx---------------------------------------------x\n")
                            case 3:
                                print(f"\nSua sugestão personalizada está pronta!\nx---------------------------------------------x\
                                    \nAlimentação Sugerida: {random.choice(repteisAlimentacao)}\nAtividade Sugerida: {random.choice(repteisAtividades)}\
                                    \nBrinquedo Sugerido: {random.choice(repteisBrinquedo)}\nx---------------------------------------------x")
                                match faixa_etaria:
                                    case 1:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_repteis_jovens)}\nx---------------------------------------------x\n")
                                    case 2:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_repteis_jovens)}\nx---------------------------------------------x\n")
                                    case 3:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_repteis_jovens)}\nx---------------------------------------------x\n")
                            case 4:
                                print(f"\nSua sugestão personalizada está pronta!\nx---------------------------------------------x\
                                    \nAlimentação Sugerida: {random.choice(peixesAlimentacao)}\nAtividade Sugerida: {random.choice(peixesAtividades)}\
                                    \nBrinquedo Sugerido: {random.choice(peixesBrinquedos)}\nx---------------------------------------------x")
                                match faixa_etaria:
                                    case 1:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_peixes_jovens)}\nx---------------------------------------------x\n")
                                    case 2:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_peixes_jovens)}\nx---------------------------------------------x\n")
                                    case 3:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_peixes_jovens)}\nx---------------------------------------------x\n")
                            
                            case 5:
                                print(f"\nSua sugestão personalizada está pronta!\nx---------------------------------------------x\
                                    \nAlimentação Sugerida: {random.choice(anfibiosAlimentacao)}\nAtividade Sugerida: {random.choice(anfibiosAtividades)}\
                                    \nBrinquedo Sugerido: {random.choice(anfibiosBrinquedos)}\nx---------------------------------------------x\n")
                                match faixa_etaria:
                                    case 1:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_anfibios_jovens)}\nx---------------------------------------------x\n")
                                    case 2:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_anfibios_jovens)}\nx---------------------------------------------x\n")
                                    case 3:
                                        print(f"Sugestão extra de cuidado: {random.choice(cuidados_anfibios_jovens)}\nx---------------------------------------------x\n")
                    elif opcoes ==2:
                        os.system('cls')
                        menuSairOuReinicio(SugestoesPersonalizadas)
                    else:
                        print("Selecione uma opção válida")


                except ValueError:
                    os.system("cls")
                    print("Digite um valor numérico!")
                    continue





