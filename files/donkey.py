with open(f"files/donkey.txt","r") as f:
    r=f.readline()
    print(r)
    print()
    a=input("enter the word you want to replace\n")
    b=input("enter new word\n")
    if a in r:
       av=r.replace(a,b)
       print(av)
       with open(f"files/donkey.txt","w") as f:
        f.write(av)

