class person:
    def __init__(self,pname,pnage):
        self.name=pname
        self.age=pnage

    def detdisplay(self):
        print("details of the person:"+self.name,self.age)

class student(person):
    def __init__(self, pname, pnage):
        person.__init__(self,pname,pnage)

x=student("jishnu",24)
x.detdisplay()
        