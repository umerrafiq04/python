import random as r

rnd= r.randint(1,10)
def guessNo(n,count):
    
   
    print(f"random number is:{rnd}\n")
    if n==rnd:
        print(f"Trials:{count}\t")
        print("You guessed it")
        
    elif rnd<n:
        print(f"just low\t Trials:{count}\n")
       
    else:
        print(f"just high\t Trials:{count}\n")
        


count=1

    