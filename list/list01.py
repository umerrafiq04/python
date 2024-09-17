from typing import List,Tuple,Dict,Union
x:list[int]=[12,1,12,123,1234,123]


def summ(s):
    print(sum(s))
    for i in s[:]:
        print(i)


summ(x[3:])