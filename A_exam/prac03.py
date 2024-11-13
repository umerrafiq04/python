def modify_value(x):
    x = 10  # This will not affect the original variable
    print("Inside function (call by value):", x)

def modify_list(lst):
    lst.append(10)  # This will modify the original list
    print("Inside function (call by reference):", lst)

# Call by value example
a = 5
print("Before function call (value):", a)
modify_value(a)
print("After function call (value):", a)

# Call by reference example
b = [5]
print("Before function call (reference):", b)
modify_list(b)
print("After function call (reference):", b)
