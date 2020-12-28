# -*- coding: utf-8 -*-

from typing import List, NoReturn

def bubble_sort(array: List) -> NoReturn:
  # Percorrendo o array com base no índice atual
  for atual, _ in enumerate(array):
    # Setando uma variável de controle para saber se existiu a troca. Inicial ela é False, pois não existiu nenhuma troca até o momento.
    exchanging = False
    # Percorrendo array do próximo índice até o final do array
    for proximo in range(atual + 1, len(array)):
      # Validando se o elemento do índice atual, armazenado na primeira iteração, é maior que os próximos elementos do restante da lista.
      if array[atual] > array[proximo]:
        # Se for maior, então o atual vira o próximo e o próximo vira o atual. Como existiu a troca, setamos exchanging como True.
        array[atual], array[proximo], exchanging = array[proximo], array[atual], True
    # Se não existir mais a troca, paramos.
    if not exchanging:
      break

def bubble_sort_alternativo(array: List) -> NoReturn:
    # Declaro uma variável chamada ordenado, para criar um loop "infinito".
    ordenado = True
    # Loop na Verdade... Perigoso...
    while ordenado:
        # Setando ordenado como False, uma vez que não ordenamos nada...
        ordenado = False
        # Percorrendo os elementos do array.
        for atual in range(len(array) - 1):
            # Pegando o próximo
            proximo = atual + 1
            # Verificando se o atual é maior que o próximo.
            if array[atual] > array[proximo]:
                # Se sim, trocamos as posições e dizemos que ordenamos.
                array[atual], array[proximo], ordenado = array[proximo], array[atual], True

if __name__ == "__main__":
    array =  [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_alternativo(array)
    print(array)
