import numpy as np
from numpy import random as rd
s=3
for i in range(s):
    x=int(input("guess the number\n"))
    z=rd.choice(rd.randint(2,5,size=(4)))
    
    print(f"guesses left:{s}\n")
    if x==z:
        print(f"you won!!\n your score={(s/3)*100}%")
        break
    s=s-1
