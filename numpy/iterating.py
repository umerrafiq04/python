import numpy as np
# arr5=np.array([[1,2,3],[7,8,9]])
# # arr6=[j*2 for j in arr5]
# # k=0
# # for i in arr6[k] :
# #     print(i)
# #     if(i==2):
#         # k=1
# # printing an array
# for i in arr5:
#     for j in i:
#         print(j)

# 3d array
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
# for i in arr:
#     for j in i:
#         for k in j:
#          print(k)

#so hectic to use n loops for n dimensional array
# The function nditer() is a helping function that can be used from very basic to very advanced iterations
# for i in np.nditer(arr):
#     print(i)
# Enumeration means mentioning sequence number of somethings one by one.

# Sometimes we require corresponding index of the element while iterating, 
# the ndenumerate() method can be used for those usecases.

arr3=np.array([1,2,3,4,5,6,7,8])
for indexx,i in np.ndenumerate(arr3):
    print(f'index={indexx}\t elementt={i}\n')

