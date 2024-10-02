import numpy as np
# def summ(a,b):
#     return a+b

# ab=np.frompyfunc(summ,2,1)
# print(summ([1,2,3,4],[1,2,3,4]))

# def mul(a,b):
#     return np.multiply(a,b)

# m=np.frompyfunc(mul,2,1)
# print(mul([1,2,3,4],[1,2,3,4]))
    

# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])

# newarr = np.mod(arr1, arr2)

# print(newarr)


# The divmod() function return both the quotient and the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.
x=np.array([10,20,30,40,50])
y=np.array([1,2,3,4,5])
print(np.divmod(x,y))