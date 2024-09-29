import numpy as np
# arr=np.array([1,2,3,4,5,56])
# print(np.where(arr==56))



arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)