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