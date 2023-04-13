# Importações:

import random as rd

# Funções:

def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    return dist


def distancia_entre_dois_pontos_3d(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^3
    Args:
      a: lista contendo as coordenadas x, y e z de um ponto.
      b: lista contendo as coordenadas x, y e z de um ponto.
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    z1 = a[2]
    z2 = b[2]
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** (1 / 2)
    return dist


def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    Args:
      n: inteiro positivo que é o número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """
    cidades = {}
    for i in range(n):
        cidades[f"Cidade {i}"] = (rd.random(), rd.random())
    return cidades


def cria_cidades_espaciais(n):
    """Cria um dicionário aleatório de estações espaciais com suas posições (x,y,z).
    Args:
      n: inteiro positivo que é o número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no espaço
      cartesiano das cidades como valores.
    """
    cidades = {}
    for i in range(n):
        cidades[f"Cidade {i}"] = (rd.random(), rd.random(),rd.random())
    return cidades


def cria_itens(n):
    """Gera um conjunto de possíveis itens e seus pesos e massas para o problema da mochila.
    Args: 
        n: inteiro positivo que é o número de itens possíveis
    Returns:
        itens: dicionário com nomes dos itens como chaves e lista com preço e peso como valores
    """
    itens = {}
    for i in range(n):
        itens[f"item {i}"] = (10*rd.random(), 10*rd.random())
    return itens


###############################################################################
#                                    Genes                                    #
###############################################################################


def gene_cb():
    """Gera um gene binário para o problema das caixas

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


def gene_liga(elementos):
    """Gera um "gene" para o problema da liga ternária.
    Args:
        elementos: lista de strings dos possíveis elementos para o gene
    Returns:
        dicionário contendo um elemento e a quantidade daquele elemento
    """
    elemento = rd.choice(elementos)
    massa = rd.uniform(0, 100)
    gene = {elemento:massa}
    return gene


###############################################################################
#                                  Indivíduos                                 #
###############################################################################


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


def individuo_liga(tamanho_liga, elementos):
    '''Gera uma liga ternária a partir de uma lista de possíveis elementos
    Args: 
        tamanho_liga: quantidade de elementos na liga (será 3 para o problema de liga ternária)
        elementos: Lista com as strings correspondentes aos nomes dos elementos que podem formar uma liga.
    Returns:
        dicionário com os elementos e suas quantidades
    '''
    ok = True
    while ok == True:
        liga = {}
        while len(liga) < tamanho_liga:
            liga.update(gene_liga(elementos))
        # normalização:
        norma = sum(liga.values())
        for k in liga:
            liga[k] = liga[k]*100/norma
        # verificando que todos são maires que 5:
        for i in liga.values():
            if i >= 5:
                ok = False #fazer nada
            else:
                ok = True
                break
    return liga


def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante
    Args:
        cidades: Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Return:
        lista de nomes de cidades formando um caminho válido.
    """
    individuo = list(cidades.keys())
    rd.shuffle(individuo)
    return individuo


def individuo_hb(xlim, ylim):
    """Gera um ponto (x,y) para o problema da função de Himmelblau
    Args:
        xlim: lista com limites inferior e superior de x
        ylim: lista com limites inferior e superior de y
    Returns:
        lista com dois valores correspondendo a x e y
    """
    x = rd.uniform(xlim[0], xlim[1])
    y = rd.uniform(ylim[0], ylim[1])
    return [x, y]


def individuo_mochila(itens):
    """Gera um indivíduo para o problema da mochila.
    Args:
        itens: Dicionário contendo os itens possíveis
    Returns:
        Lista dos itens contidos na mochila
    """
    individuo = []
    for i in list(itens.keys()):
        if rd.randint(0,1) == 1:
            individuo.append(i)
    return individuo


###############################################################################
#                                  População                                  #
###############################################################################
    

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


def populacao_inicial_liga(tamanho, tamanho_liga, elementos):
    """Cria população inicial no problema da liga ternária
    Args
      tamanho: tamanho da população.
      tamanho_liga: quantidade de elementos na liga (será 3 para o problema de liga ternária)
      elementos: Lista com as strings correspondentes aos nomes dos elementos que podem formar uma liga.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_liga(tamanho_liga, elementos))
    return populacao


def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    Args
        tamanho: Tamanho da população.
        cidades: Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
        Lista com todos os indivíduos da população no problema do caixeiro
        viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


def populacao_inicial_hb(tamanho, xlim, ylim):
    """Cria população inicial para o problema da função de Himmelblau
    Args: 
        tamanho: tamanho da população
        xlim: lista com limites inferior e superior de x
        ylim: lista com limites inferior e superior de y
    Returns:
        população que é uma lista de pontos (x,y)
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_hb(xlim, ylim))
    return populacao


def populacao_inicial_mochila(tamanho, itens):
    """Cria população inicial para o problema da mochila
    Args: 
        tamanho: tamanho da população
        itens: Dicionário contendo os itens possíveis
    Returns:
        população que é uma lista de indivíduos (mochilas)
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_mochila(itens))
    return populacao    


###############################################################################
#                                   Seleção                                   #
###############################################################################


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
        maximo_fitness = -float("inf")
        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]
            if fit > maximo_fitness:
                selecionado = individuo
                maximo_fitness = fit
        selecionados.append(selecionado)
    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


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


def cruzamento_liga(pai, mae):
    """Operador de cruzamento para duas ligas
    Args:
        pai: um dicionário correspondente a um individuo
        mae: um dicionário correspondente a um individuo
    Returns:
        Dois dicionários: sendo que cada um representa um filho dos pais que foram os qrgumentos.
    """
    chaves = set(list(pai.keys()) + list(mae.keys()))
    elementos1 = rd.sample(chaves, len(pai))
    elementos2 = rd.sample(chaves, len(mae))
    quantidades1 = list(pai.values())
    quantidades2 = list(mae.values())
    filho1, filho2 = {},{}
    for elemento, quantidade in zip(elementos1, quantidades1):
        filho1.update({elemento : quantidade})
    for elemento, quantidade in zip(elementos2, quantidades2):
        filho2.update({elemento : quantidade})
    return filho1, filho2


def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.
    
    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.

    Ver pág. 37 do livro do Wirsansky.

    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo

    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = rd.randint(0, len(pai)-2)
    corte2 = rd.randint(corte1+1, len(pai)-1)
    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
    return filho1, filho2


def cruzamento_subconjunto(pai, mae):
    """Operador de cruzamento para listas onde a ordem não importa
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais
      que foram osargumentos. Uma possui o mesmo tamanho que o pai 
      e a outra o mesmo tamanho que a mãe
    """
    elementos = list(set(pai + mae))
    rd.shuffle(elementos)
    filho1 = rd.sample(elementos, len(pai))
    filho2 = rd.sample(elementos, len(mae))
    return filho1, filho2
    

###############################################################################
#                                   Mutação                                   #
###############################################################################


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


def mutacao_elemento_liga(individuo, elementos):
    """Realiza a mutação de um elemento no problema da liga ternaria.
    Args:
      individuo: dicionario corespondente aos elementos e quantidades em uma liga
      elementos: strings dos possíveis elementos para a liga
    Return:
      Um individuo (liga) com um gene mutado.
    """
    quantidades = list(individuo.values())
    indice = rd.randint(0, len(individuo) - 1)
    elemento = list(individuo.keys())[indice]
    quantidade = individuo[elemento]
    del individuo[elemento]
    while len(individuo)<3:
        novo_elemento = rd.choice(elementos)
        individuo.update({novo_elemento:quantidade})
    k=0
    for i in individuo:
        individuo[i] = quantidades[k]
        k = k+1
    return individuo


def mutacao_quantidades_liga(individuo):
    """Realiza a mutação das quantidades no problema da liga ternária.
    Args:
      individuo: dicionario corespondente aos elementos e quantidades em uma liga
    Return:
      Um individuo (liga) com as quantidades mutadas.
    """
    elementos = list(individuo.keys())
    ok = True
    while ok == True:
        liga = {}
        h = 0
        while len(liga) < len(individuo):
            liga.update({elementos[h]:rd.uniform(0,100)})
            h = h+1
        # normalização:
        norma = sum(liga.values())
        for k in liga:
            liga[k] = liga[k]*100/norma
        # verificando que todos são maires que 5:
        for i in liga.values():
            if i >= 5:
                ok = False #fazer nada
            else:
                ok = True
                break
    return liga
    elementos = list(individuo.keys())
    individuo = {}
    for elemento, quantidade in zip(elementos, quantidades):
        individuo.update({elemento:quantidade})    
    return individuo


def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.
    Args:
      individuo: uma lista representado um individuo.
    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    indices = list(range(len(individuo)))
    lista_sorteada = rd.sample(indices, k=2)
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    individuo_mutado = individuo.copy()
    individuo_mutado[indice1] = individuo[indice2]
    individuo_mutado[indice2] = individuo[indice1]
    return individuo_mutado


def mutacao_hb(individuo, step_maximo):
    """Realiza mutação em um ponto (x,y) da função de Himmelblau.
    Args:
        individuo: lista que corresponde a um ponto (x,y)
        step_maximo: distância máxima que o ponto pode ser mutado, em x ou em y
    Returns: 
        individuo mutado
    """
    gene = rd.randint(0, len(individuo) - 1)
    individuo[gene] = rd.uniform(individuo[gene] - step_maximo, individuo[gene] + step_maximo)
    return individuo


def mutacao_mochila(individuo, itens):
    """Operador de mutação para a mochila
    Args:
        indiviuo: lista de itens na mochila
        itens: dicionário dos itens possíveis
    Returns:
        individuo mutado
    """
    itens_disponiveis = []
    for i in list(itens.keys()):
        if i not in individuo:
            itens_disponiveis.append(i)
    tipo = rd.randint(0,2)
    if tipo == 0 or len(itens_disponiveis) == 0:
        if len(individuo) > 1:
            individuo.remove(individuo[rd.randint(0, len(individuo)-1)])
    elif tipo == 1 and len(itens_disponiveis) > 0:
        individuo.append(itens_disponiveis[rd.randint(0, len(itens_disponiveis)-1)])
    elif len(itens_disponiveis) > 0: 
        individuo.remove(individuo[rd.randint(0, len(individuo)-1)])
        individuo.append(itens_disponiveis[rd.randint(0, len(itens_disponiveis)-1)])
    return individuo


###############################################################################
#                         Função objetivo - indivíduos                        #
###############################################################################


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



def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """
    distancia = 0
    k = 0
    while k<len(individuo):
        distancia += distancia_entre_dois_pontos(cidades[individuo[k-1]], cidades[individuo[k]])
        k+=1
    # preencher o código
    return distancia


def funcao_objetivo_cva(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante astronauta.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas (x,y,z) das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """
    distancia = 0
    k = 0
    while k<len(individuo):
        distancia += distancia_entre_dois_pontos_3d(cidades[individuo[k-1]], cidades[individuo[k]])
        k+=1
    # preencher o código
    return distancia


def himmelblau(individuo):
    """Computa a função de Himmelblau em um ponto (x,y)
    Args: 
        individuo: lista com x e y
    Returns:
        Valor da função de Himmelblau no ponto
    """
    x = individuo[0]
    y = individuo[1]
    z = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    return z


def funcao_objetivo_mochila(individuo, itens, p):
    """Computa a função objetivo de uma muchila, que é a soma
    dos valores dos itens, mas é 0 caso o pesoseja maior que um
    limite
    Args:
        individuo: lista dos itens na mochila
        itens: dicionário dos itens possíveis
        p: limite de peso que a mochila aguenta
    Returns:
        número função objetivo da mochila

    """
    pesos = []
    for i in individuo:
        peso = itens[i][1]
        pesos.append(peso)
    if sum(pesos)> p:
        return 0
    else:
        valores = []
        for i in individuo:
            valor = itens[i][0]
            valores.append(valor)
        return sum(valores)
    
    
###############################################################################
#                         Função objetivo - população                         #
###############################################################################


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


def funcao_objetivo_pop_cv(populacao, cidades):
    """Calcula a função objetivo para todos os individuos da população.
    Args:
        populacao: Lista com todos os individuos
    Returns:
        Lista com os fitness de cada individuo da populacao
    """
    fobj = []
    for individuo in populacao:
        fobj.append(funcao_objetivo_cv(individuo, cidades))
    return fobj


def funcao_objetivo_pop_cva(populacao, cidades):
    """Calcula a função objetivo para todos os individuos da população.
    Args:
        populacao: Lista com todos os individuos
    Returns:
        Lista com os fitness de cada individuo da populacao
    """
    fobj = []
    for individuo in populacao:
        fobj.append(funcao_objetivo_cva(individuo, cidades))
    return fobj


def funcao_objetivo_pop_hb(populacao):
    """Computa a funcao objetivo de uma populaçao no problema de Himmelblau.
    Args:
        populacao: lista com todas as ligas da população.
    Returns:
      Lista contendo os valores da função de Himmelblau dos pontos.
    """
    resultado = []
    for individuo in populacao:
        resultado.append(himmelblau(individuo))
    return resultado


def funcao_objetivo_pop_mochila(populacao, itens, p):
    """Computa a função objetivo de uma população de mochilas
    Args:
        populacao: lista com todas as mochilas da população
        itens: dicionário dos itens possíveis
        p: limite de peso que a mochila aguenta
    Returns:
        lista dos números função objetivo das mochilas
    """
    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_mochila(individuo, itens, p))
    return resultado