#greatest of 3
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
    
# print(greatest(12,23,45))

# *** n=3
# **        c=2.333333333
# *         round(c,2) 2.33

# def pattern(n):
#     for i in range(3,0,-1): 
#             print("*"*i)

# pattern(3) 
# 
# using recursion
        
def pattern(n):
    if(n==0):
            return
    print("*"*n)  
    pattern(n-1)  

pattern(3)         