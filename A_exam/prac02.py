# no=int(input("enter the number\n"))
# p=int(input("enter the power\n"))

# def power(x,y):
#     # return no**p
#     r=1
#     for i in range(p):
#         r=r*x
#     return r

# print(power(no,p))

#gcd of two numbers
# a=60
# b=36

# def gcd(a,b):

#     if(a>b):
#         min=b
#     else:
#         min=a
#     max=1    
#     for i in range(1,min+1):
#           if(a%i==0 and b%i==0):
#               if(i>max):
#                   max=i
#     return max              

# print(gcd(a,b))

# Euclid's algorithm.
# def gcd(a, b):
#     while b:
#         a, b = b, a%b
#     return a

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"GCD of {num1} and {num2} is {gcd(num1, num2)}")


# for i in range(1,100):
#     max=int(i/2)+1
#     count=0
#     for j in range(1,max):
#         if(i%j==0):
#             count=count+1
#     if(count<2):
#         print(f"{i}\t")   
#      
# def isprime(x):
#     i=2
#     if x==1:
#         return False
#     while i < int(x/2)+1:
#         if x%i==0:
#             return False
#         i+=1
#     return True    


# def fnp(n):
#     prime=[]
#     num=2
#     while len(prime)<n:
#         if isprime(num):
#             prime.append(num)
#         num+=1
#     return prime     
# print(fnp(10))

# def rec(n):
#     fact=1
#     if n==1:
#         return 1

#     fact*=rec(n-1)
#     return fact
# print(rec(4))
