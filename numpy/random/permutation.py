# A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# The NumPy Random module provides two methods for this: shuffle() and permutation().



from numpy import random as rd
import numpy as np
arr1=np.array([1,2,3,4,5,6])
print(f"before shuffle:{arr1}\n")
rd.shuffle(arr1) #The shuffle() method makes changes to the original array.
print(f"after shuffle:{arr1}\n") #The array is shuffled in-place, meaning that the original array is modified.


#permutation
print(f"before shuffle:{arr1}\n")
arr2=rd.permutation(arr1)
print(f"after shuffle:{arr1}\n")
print(f"new array:{arr2}\n")