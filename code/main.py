from functions import base
from library import sort

if __name__ == "__main__":
  array =  [22, 100, 4, 46, 99, 50, 2, -1, 17, 5, 23, 1, 82, 3]
  sort = sort.Sort()

  print(f"Base sort:      {base.base_sort(array)}")
  print(f"Bubble sort:    {sort.bubble_sort(array)}")
