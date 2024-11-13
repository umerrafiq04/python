arr=[1,2,3,4,5,6]

# def ls(x):
#     flag=0
#     for i in arr:
#         if i==x:
#             print(arr.index(x))
#             flag=1
#     if(flag==0):
#         print("element not present")      


# ls(69)

def bs(l,h,x):
    mid=int((l+h)/2)
    if(x<=arr[h] and x>=arr[l]):
        if(arr[mid]==x):
            print(f"index={arr.index(arr[mid])},index={arr.index(x)}")
        elif(x>arr[mid]):
            bs(mid+1,h,x)
        elif(x<arr[mid]):
            bs(l,mid-1,x)   
         
    else:
        print("element not found\t")   


bs(0,5,-16)


