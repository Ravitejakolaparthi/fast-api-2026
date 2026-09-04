# generic type hints are of types that made to use for type for list
# Simply internal types
#
# Tuple -> ()
# list -> []
# set -> <>
# dict -> {}#
# this also used for better editor support
from typing import List
def Example(lis : list[int]):
    for i in lis:
        print(i,end=" ")

Example([1,2,3,4,5])