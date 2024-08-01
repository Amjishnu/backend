class person:
    def __init__(self ,name,age):
        self.a= name
        self.b = age

    def greet(self):
        print(f"Hello,my nsme is{self.a} and i am {self.b} years old.")

person1 = person("jishnu",24)


person1.greet()