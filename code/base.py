# -*- coding: utf-8 -*-

"""Documentation file base.py."""

# =============================================================================
# IMPORTS
# =============================================================================

try:
    from typing import List
except ImportError as error:
    print("""
    The module {0} is missing.
    Try something like: pip install {0}""".format(error.name))

# =============================================================================
# FUNCTIONS
# =============================================================================

def base_sort(array: List) -> List:
    return sorted(array, reverse=False)

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    array =  [22, 46, 50, 17, 5, 23, 1, 82, 3]
    print(base_sort(array))
