import random as r

def game():
    score= r.randint(1,100)
    print(f"your score {score} \t")
    with open("game.txt") as f:
        hs=(f.read())
       
        if(hs!=""):
            hs=int(hs)
        
        else:
            hs=0  
        print(f"high score {hs} \t")
    if(score>hs):
          with open("game.txt","w") as f:
              f.write(str(score))
    return score           

game()