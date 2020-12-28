# -*- coding: utf-8 -*-

try:
    from typing import List, NoReturn
except ImportError as error:
    print("""
    The module {0} is missing.
    Try something like: pip install {0}""".format(error.name))

# =============================================================================
# FUNCTIONS
# =============================================================================

def selection_sort(array: List) -> NoReturn:
    # Percorrendo o array com base no índice atual
    for atual, _ in enumerate(array):
        # Setando o menor elemento com o elemento do índice atual.
        menor = atual
        # Percorrendo array do próximo índice até o final do array
        for proximo in range(atual + 1, len(array)):
            # Se o próximo elemento for menor que o elemento do índice menor, então o menor é o próximo índice.
            if array[proximo] < array[menor]:
                # Setamos o índice do menor elemento como o índice do próximo.
                menor = proximo
        # Trocamos os elementos
        array[atual], array[menor] = array[menor], array[atual]

# =============================================================================

def selection_sort_alternative(array: List) -> NoReturn:
    # Percorremos o array ignorando o último elemento.
    for index_atual, _ in enumerate(array[:-1]):
        # Seta o índice do menor elemento como o índice do elemento atual.
        index_menor = index_atual
        # Pecorre o array na posição do index_atual, que está ignorando o último elemento, até o final.
        for index_proximo, _ in enumerate(array[index_atual::]):
            # Checa se o elemento da lista total é menor do que o elemento do índice menor.
            if _ < array[index_menor]:
                # Se for, setamos o índice menor.
                index_menor = index_proximo
        # Trocamos.
        array[index_atual], array[index_menor] = array[index_menor], array[index_atual]

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    array =  [5, 3, 1]
    selection_sort_alternative(array)
    print(array)
