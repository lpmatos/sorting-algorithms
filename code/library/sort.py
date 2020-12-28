from typing import List, NoReturn
from dataclasses import dataclass, field

@dataclass
class Sort:
  swap: int = field(default=1, repr=False)

  def bubble_sort(self, array: List) -> NoReturn:
    while self.swap:
      self.swap = 0
      for atual in range(len(array) - 1):
        if array[atual] > array[atual + 1]:
          array[atual], array[atual + 1], self.swap = array[atual + 1], array[atual], 1
    return array
