# -*- coding: utf-8 -*-

"""Documentation file selection.py."""

# =============================================================================
# IMPORTS
# =============================================================================

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
# MAIN
# =============================================================================

if __name__ == "__main__":
    array =  [64, 34, 25, 12, 22, 11, 90]
    selection_sort(array)
    print(array)
