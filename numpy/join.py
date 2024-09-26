import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr11 = np.concatenate((arr1, arr2), axis=1) #adds in only one way
arr22 = np.hstack((arr1, arr2)) #it can be done along any axis
arr23 = np.stack((arr1, arr2),axis=0) #default=0
arr234 = np.stack((arr1, arr2),axis=1) 
arrv = np.vstack((arr1, arr2)) 
arrd= np.dstack((arr1, arr2))
print(f"concatenate:\n{arr11}\n")
print(f"hstack:\n{arr22}\n")
print(f"stack(axis=0):\n{arr23}\n")
print(f"stack(axis=1):\n{arr234}\n")
print(f"vstack:\n{arrv}\n")
print(f"depth:\n{arrd}\n")

