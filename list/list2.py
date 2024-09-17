# # a=list(range(10))
# # print(a)
# # print(type(a))
# # l2=[str(c) for c in a]
# # print(l2)
# # arr2=[]
# # arr=[]
# # for i in range(10):
# #     arr.append(i)

# # print(f"arr1:{arr}")

# # print("arr2:\t")
# # print([n*n for n in arr])

# # print("type of arr2:")
# # print([type(item) for item in arr2])


# # lis=[10,11,12,13,12,123,45,6]
# # print(type(lis))
# # print(len(lis))
# # #print(2*(lis))

# # #print([i*i for i in lis])
# # print([i*i for i in lis if i%2==0])


# # if(3>2) >1:
# #     print("true")

# # else:
# #     print("false")   

# # import sys

# # print(sys.version)


# # for k in [j*j for j in [i**3 for i in [2,3,4,5,6,7]]]:
# #     print(k)
 
# # a=["apple","banana","tiger"]
# # x,y,z=a
# # print(x)

# # def fun():
# #     global x
# #     x=[i*2 for i in range(1,6)]
    
    
# # fun()
# # print(x)
# import tkinter as tk
# from tkinter import messagebox

# # Function to check login credentials
# def login():
#     username = entry_username.get()
#     password = entry_password.get()

#     # Simple validation for demonstration
#     if username == "admin" and password == "password":
#         messagebox.showinfo("Login", "Login Successful!")
#     else:
#         messagebox.showerror("Login", "Invalid credentials, please try again.")

# # Create the main window
# root = tk.Tk()
# root.title("Login Interface")
# root.geometry("300x200")

# # Username label and text entry box
# label_username = tk.Label(root, text="Username")
# label_username.pack(pady=5)
# entry_username = tk.Entry(root)
# entry_username.pack(pady=5)

# # Password label and text entry box
# label_password = tk.Label(root, text="Password")
# label_password.pack(pady=5)
# entry_password = tk.Entry(root, show="*")
# entry_password.pack(pady=5)

# # Login button
# login_button = tk.Button(root, text="Login", command=login)
# login_button.pack(pady=20)

# # Run the application
# root.mainloop()


