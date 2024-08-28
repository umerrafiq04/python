# will generate tables and save them in a tables named folder
def table(n):
         with open(f"tables/table{n}.txt","w") as f:
                f.write(f"Table of {n}:\n")
                for  i in range(1,10):
                  f.write(f"{n}*{i}={i*n}\n")
 
for i in range(10):
       table(i) 


