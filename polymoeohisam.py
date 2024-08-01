class sum:
    def __init__(self,fnum,snum):
        self.fn=fnum
        self.sn=snum

    def display(self):
        print("sum is :",self.fn+self.sn)

class diff:
    def __init__(self,fnum,snum):
        self.fn=fnum
        self.sn=snum

    def display(self):
        print("difference is :",self.fn+self.sn)


class pdf:
    def __init__(self,fnum,snum):
        self.fn=fnum
        self.sn=snum

    def display(self):
        print("product is :",self.fn+self.sn)

class qnt:
    def __init__(self,fnum,snum):
        self.fn=fnum
        self.sn=snum

    def display(self):
        print("quotient is :",self.fn+self.sn)

a=sum(2,4)
b=diff(4,5)
c=pdf(3,5)
d=qnt(25,8)

a.display()
b.display()
c.display()
d.display()
     