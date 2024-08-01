class person:
    def __init__(self,pname,pnage):
        self.name=pname
        self.age=pnage

    def detdisplay(self):
        print("details of the person:"+self.name,self.age)

class student(person):
    def __init__(self, pname, pnage,pyear):
        super().__init__(pname,pnage)
        self.year=pyear

    def detprint(self):
         print("details of the person:"+self.name,self.age,self.year)
     

x=student("jishnu",24,2000)
print(x.year)

x.detdisplay()
x.detprint()