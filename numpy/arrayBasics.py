import numpy as np
# arr1=np.array([1,2,3,4,5,6],ndmin=4)
# print(arr1)
# print(arr1.ndim)

# arr2=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr2[0,2]+arr2[1,2])

# '''slicing'''
# arr=np.array([1,2,3,4,5,6])
# print(arr[:3:2])
# # 2d slicing
# arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr3[1, 1:4])

# arr3=np.array([[1,2,3,5,6,7,8,8],[5,4,345,34,5,6,7,77]])
# print(arr3[0:2,:4])

# arr=np.array([1,2,3,4,5,6])
# # for i in arr:
# #     print(i)
# print(arr.dtype)

arr2=[1,2,3,4,5,6]
arr3=np.array(arr2,dtype="i") #or arr3 = arr2.astype(int)

print(arr3.dtype)