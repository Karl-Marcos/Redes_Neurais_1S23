# Importações:

import random as rd


# Funções:


def gene_cb():
    """Gera um gene binario para o problema das caixas

    Return:
        Valor zero ou um
    """
    lista = [0, 1]
    return rd.choice(lista)


def gene_cnb(valor_max_caixa):
    """Gera um gene para o problema das caixas não-binárias
    Args:
      valor_max_caixa: número inteiro representando o maior valor possível que
      pode existir dentro de uma caixa.
    Return:
      Um valor entre zero e o valor máximo da caixa.
    """
    gene = rd.randint(0, valor_max_caixa)
    return gene


def gene_letra(letras):
    """Sorteia uma letra
    Args:
      letras: lista de letras que podem ser sorteadas
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas
    """
    letra = rd.choice(letras)
    return letra


def individuo_cb(n):
    """Gera um individuo para o problemas de caixas

    Args:
        n: numero de genes

    Return:
        Uma lista com n genes, cada um com um valor 0 ou 1
    """

    individuo = []

    for i in range(n):
        individuo.append(gene_cb())
    return individuo


def individuo_cnb(n_genes, valor_max_caixa):
    """Gera um individuo para o problema das caixas não-binárias.
    Args:
      n_genes: número de genes do indivíduo.
      valor_max_caixa: número inteiro representando o maior valor possível que
      pode existir dentro de uma caixa.
    Return:
       Uma lista com n genes. Cada gene é um valor entre zero e
       `valor_max_caixa`.
    """
    individuo = []
    for i in range(n_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo


def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato


def populacao_cb(tamanho, n):
    """Cria uma população no problema de caixas binarias

    Args:
        n: numero de genes
        tamanho: numero de individuos

    Returns:
        Uma lista onde cada item é um individuo
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao


def populacao_cnb(tamanho, n_genes, valor_max_caixa):
    """Cria uma população para o problema das caixas não-binárias.
    Args:
      tamanho: tamanho da população.
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa
    Returns:
      Uma lista onde cada item é um indiviuo. Um individuo é uma lista com
      `n_genes` genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cnb(n_genes, valor_max_caixa))
    return populacao


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao


def selecao_roleta_max(populacao, fitness):
    """Seleciona indivíduos de uma população usando o metodo da roleta.
    Nota: Apenas funciona para problemas de maximização.

    Args:
        populacao: lista com todos os individuos da populacao
        fitness: lista dos valores da funcao objetivo

    Returns:
        Populacao dps individuos selecionados
    """
    # arrumando bug de weights nulos:
    if sum(fitness) == 0:
        fitness_novo = []
        for _ in fitness:
            fitness_novo.append(1)
    else:
        fitness_novo = fitness
    # fazendo a seleção
    populacao = rd.choices(populacao, weights=fitness_novo, k=len(populacao))
    return populacao


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos indivíduos
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    par_populacao_fitness = list(zip(populacao, fitness))

    for _ in range(len(populacao)):
        combatentes = rd.sample(par_populacao_fitness, tamanho_torneio)

        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados


def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples
    Args:
        pai: uma lista correspondente a um individuo
        mae: uma lista correspondente a um individuo


    Returns:
        Duas listas: sendo que cada uma representa um filho dos pais que foram os qrgumentos.
    """
    ponto_de_corte = rd.randint(1, len(mae) - 1)

    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]

    return filho1, filho2


def mutacao_cb(individuo):
    """Realiza uma mutação em um individuo para o problema de caixas binárias

    Args:
        individuo: individuo onde vai ocorrer a mutacao

    Returns:
        individuo após a mutação
    """
    gene_para_mutar = rd.randint(0, len(individuo) - 1)
    individuo[gene_para_mutar] = gene_cb()
    return individuo


def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação de um gene para o problema das caixas não-binárias
    Args:
      individuo:
        uma lista representado um individuo no problema das caixas não-binárias
      valor_max_caixa:
        maior número inteiro possível dentro de uma caixa
    Return:
      Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = rd.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo


def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = rd.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo


def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binarias

    Args:
        individuo: Lista contendo os genes

    Return:
        Soma dos genes do individuo
    """
    s = 0
    for i in individuo:
        s = s + i
    return s


def funcao_objetivo_pop_cb(populacao):
    """Calcula a função objetivo para todos os individuos da população.

    Args:
        populacao: Lista com todos os individuos

    Returns:
        Lista com os fitness de cada individuo da populacao
    """
    fobj = []
    for individuo in populacao:
        fobj.append(funcao_objetivo_cb(individuo))
    return fobj


def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado

def liga_ternaria(elementos):
    '''Gera uma liga ternária a partir de uma lista de possíveis elementos
    Args: 
        elementos: Lista com as strings correspondentes aos nomes dos elementos que podem formar uma liga.
    Returns:
        dicionário com os elementos e suas quantidades
    '''
    elementos_escolhidos = rd.sample(elementos, 3)
    x = 0; y = 0; z = 0
    
    while x < 5 or y<5 or z < 5:
        x = rd.uniform(5, 100)
        y = rd.uniform(5, 100) - x
        z = 100 - x - y
    xyz = [x,y,z]
    liga = {}
    for i in elementos_escolhidos:
        liga[i] = xyz[elementos_escolhidos.index(i)]
    return liga

def populacao_inicial_liga(tamanho, elementos):
    """Cria população inicial no problema da liga ternaria
    Args
      tamanho: tamanho da população.
      elementos: Lista com as strings correspondentes aos nomes dos elementos que podem formar uma liga.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(liga_ternaria(elementos))
    return populacao

def preco_liga(liga, preco):
    '''Calcula o preco de uma liga ternaria a partir da lista de preços de cada elemento
    Args:
        liga: dicionário com elementos e quantidades
        preco: dicionario com os precos de cada elemento:
    Returns:
        preco da liga
    '''
    preco_total = 0
    
    for i in liga:
        preco_total = preco_total + float(liga[i])*float(preco[i])/1000
    return preco_total

def funcao_objetivo_pop_liga(populacao, preco):
    """Computa a funcao objetivo de uma populaçao no problema da lista.
    Args:
        populacao: lista com todas as ligas da população
        preco: dicionario com os precos de cada elemento:
    Returns:
      Lista contendo os valores de preco das ligas
    """
    resultado = []

    for liga in populacao:
        resultado.append(preco_liga(liga, preco))

    return resultado


def selecao_torneio_max(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    maximização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos indivíduos
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    par_populacao_fitness = list(zip(populacao, fitness))

    for _ in range(len(populacao)):
        combatentes = rd.sample(par_populacao_fitness, tamanho_torneio)

        maximo_fitness = 0

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            if fit > maximo_fitness:
                selecionado = individuo
                maximo_fitness = fit

        selecionados.append(selecionado)
    return selecionados


def mutacao(liga, preco):
    
    