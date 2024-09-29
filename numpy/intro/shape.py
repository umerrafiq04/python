import numpy as np
# arr=np.array((1,2,3,4,5,6))
# x=arr.copy()
# y=arr.view()
# # base returns parent.since copy(x) owns data,it will return none
# print(x.base)
# print(y.base)

# 


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]],ndmin=2)

print(arr.shape)
print(arr.ndim)
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3.shape)