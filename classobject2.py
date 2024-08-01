class vishnu:
    def inpt(jk,x,y):
        jk.num1 = x
        jk.num2 = y

    def sum(jk):
        print("sum :",jk.num1+jk.num2)

    def dif(jk):
        print("diffrence :",jk.num1-jk.num2)
        
    def pdt(jk):
        print("product :",jk.num1*jk.num2)

    def qnt(jk):
        print("quotient:",jk.num1/jk.num2)

a=vishnu()
b=vishnu()

a.inpt(4,6)
b.inpt(5,6)

a.sum()
b.sum()

a.dif()
b.dif()

a.pdt()
b.pdt()

a.qnt()
b.qnt()