class Arith:
    n1,n2 = 0,0
    def __init__(self,a,b):
        self.n1,self.n2 = a,b
    
    def add(self):
        add = self.n1 + self.n2
        return add

    def sub(self):
        sub = self.n1 +-self.n2
        return sub

    def mul(self):
        mul = self.n1 * self.n2
        return mul

    def div(self):
        div = self.n1 / self.n2
        return div

a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))    
ari = Arith(a,b)
print("Sum is ",ari.add(),"\nDifference is ",ari.sub(),"\nMultiplication is ",ari.mul(),"\nDivision is ",ari.div())