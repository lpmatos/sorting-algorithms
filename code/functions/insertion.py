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

def insertion_sort(array: List) -> NoReturn:
    for index_atual, elemento_atual in enumerate(array):
        while index_atual != 0 and array[index_atual - 1] > elemento_atual:
            array[index_atual] = array[index_atual - 1]
            index_atual -= 1
        array[index_atual] = elemento_atual

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    array =  [22, 46, 50, 17, 5, 23, 1, 82, 3]
    insertion_sort(array)
    print(array)
