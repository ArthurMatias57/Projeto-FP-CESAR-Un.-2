import os

CAMINHO_AMBIENTE = os.path.join("Projeto-FP-CESAR-Un.-2\src\BD\BDambiente.txt")


def criar_arvore(caminho_arquivo):
    arvore = {}
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            if linha.strip().startswith("#") or not linha.strip():
                continue  # Ignora comentários e linhas vazias
            dados = linha.strip().split('|')
            if len(dados) != 7:
                continue  # Ignora linhas mal formatadas
            raca, grupo, especie, nome_pop, caracteristicas, rec_gen, rec_esp = dados
            caracteristicas = [c.strip().lower() for c in caracteristicas.split(',')]

            if raca not in arvore:
                arvore[raca] = {"grupos": {}}
            if grupo not in arvore[raca]["grupos"]:
                arvore[raca]["grupos"][grupo] = {
                    "caracteristicas": caracteristicas,
                    "recomendacao_generica": rec_gen.strip(),
                    "especies": {}
                }
            arvore[raca]["grupos"][grupo]["especies"][especie] = {
                "nome_popular": nome_pop.strip(),
                "recomendacao": rec_esp.strip()
            }
    return arvore

def imprimir_arvore(arvore):
    for raca, dados_raca in arvore.items():
        print(f"Raça: {raca}")
        for grupo, dados_grupo in dados_raca["grupos"].items():
            print(f"  Grupo: {grupo}")
            print(f"    Características: {', '.join(dados_grupo['caracteristicas'])}")
            print(f"    Recomendação Genérica: {dados_grupo['recomendacao_generica']}")
            for especie, dados_especie in dados_grupo["especies"].items():
                print(f"      Espécie: {especie} ({dados_especie['nome_popular']})")
                print(f"        Recomendação Específica: {dados_especie['recomendacao']}")


def recomendar_ambiente(arvore):
    raca = input("Digite a raça do seu pet (ex: Cachorro, Gato, Lagarto): ").strip()
    especie = input("Digite a espécie do seu pet (ou pressione Enter se não souber): ").strip()
    caracteristicas_input = input("Digite características físicas do seu pet, separadas por vírgula (ex: ativo, sociável): ").strip()
    caracteristicas = [c.strip().lower() for c in caracteristicas_input.split(',')]

    if raca not in arvore:
        print("Raça não encontrada no sistema.")
        return

    grupos = arvore[raca]["grupos"]
    grupo_encontrado = None
    for grupo, dados_grupo in grupos.items():
        if all(c in dados_grupo["caracteristicas"] for c in caracteristicas):
            grupo_encontrado = grupo
            break

    if not grupo_encontrado:
        print("Nenhum grupo encontrado com as características fornecidas.")
        return

    print(f"\nRecomendação Genérica para o grupo '{grupo_encontrado}':")
    print(grupos[grupo_encontrado]["recomendacao_generica"])

    if especie:
        especies = grupos[grupo_encontrado]["especies"]
        if especie in especies:
            print(f"\nRecomendação Específica para a espécie '{especie}' ({especies[especie]['nome_popular']}):")
            print(especies[especie]["recomendacao"])
        else:
            print("Espécie não encontrada no grupo fornecido.")
#imprimir_arvore(criar_arvore(CAMINHO_AMBIENTE))
recomendar_ambiente(criar_arvore(CAMINHO_AMBIENTE))