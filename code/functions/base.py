# -*- coding: utf-8 -*-

from typing import List, Any

def base_sort(array: List[Any]) -> List:
  """
  Function that sorts elements using python built-in functions.

  :param array: An array (List) with Any N elements.
  :return: A list with the ordered elements.
  """
  return sorted(array, reverse=False)

if __name__ == "__main__":
  array =  [22, 100, 4, 46, 99, 50, 2, 17, 5, 23, 1, 82, 3]
  print(base_sort(array))
