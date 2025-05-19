def criandoAmbiente():
    #Basicamente, a funcionalidade vai importar do arquivo a espécie. Vou fazer uma espécie de árvore de recomendações, com 
    #uma hierarquia na qual no topo estão as raças, com recomendações mais genéricas, e mais especificas. Posso implementar
    #uma árvore para gerar as recomendações. Talvez um parametro pedindo características do animal possa ser suficiente para
    #especificar mais e gerar as recomendações.  

    """
    Frame 1:
        Digite a espécie do seu pet:
        Digite a raça dele:

        Espécie não está registrada no sistema. Recomendação mudará
        Filtro1: Seu pet possui {característica} ??
        Filtro2: seu pet possui se reproduz {caracteristica} ??

        Aqui a recomendação:
    """

    print("Geracao de ambiente ideal:")

def leituraCriacaoArv(caminho_arquivo = "dados/ambientes_ideais.txt"):
    """
    Aqui, implemento a árvore, atribuindo cada ponteiro do arquivo como sendo um indice da árvore. Assim vai funcionar o acesso aos textos do arquivo. Vou pedir ao chat que monte o arquivo contendo as espécies e os indices de cada caracteristica, como se fossem objetos. 

    """
    arvore = {}
    especie_atual = None
    raca_atual = None

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith("Espécie:"):
                especie_atual = linha.split("Espécie:")[1].strip()
                arvore[especie_atual] = {}
            elif linha.startswith("Raça:"):
                raca_atual = linha.split("Raça:")[1].strip()
                arvore[especie_atual][raca_atual] = {}
            elif ":" in linha and especie_atual and raca_atual:
                chave, valor = linha.split(":", 1)
                arvore[especie_atual][raca_atual][chave.strip()] = valor.strip()
    return arvore

def imprimir_arvore(arvore, nivel=0):
    """
    Função para imprimir a arvore como se encontra no momento (função apenas para debug e referenciação)

    """

    indent = "    " * nivel
    if isinstance(arvore, dict):
        for chave, valor in arvore.items():
            print(f"{indent}{repr(chave)}:")
            imprimir_arvore(valor, nivel + 1)
    elif isinstance(arvore, list):
        for item in arvore:
            print(f"{indent}- {item}")
    else:
        print(f"{indent}{repr(arvore)}")
