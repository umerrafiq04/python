import numpy as np
from numpy import random as rn

# arr=rn.randint(3,10,size=(5))
# arr=rn.randint(3,10,size=(3,4))
for i in range(10):
    arr=rn.choice([1,2,3,4,5,6,7,7],size=(2,3))
    print(arr)