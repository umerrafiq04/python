# findin square cube and underroot of  a number
class caluclator:
    def __init__(self,n):
        self.n=n
        sq=self.n*self.n
        cu=self.n**3
        rt=self.n**(1/2)
        print(f"square:{sq}\n")
        print(f"Cube:{cu}\n")
        print(f"Root:{rt}\n")
    # def square(self):
    
    #     sq=self.n*self.n
    #     print(sq)


sqr= caluclator(3)
# sqr.square()
#reduce code by reducing the burden of functions. just use con