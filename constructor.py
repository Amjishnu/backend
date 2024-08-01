class person:
    def __init__(self):
        self.name = input("Enter ur name:")
        self.age =int(input("Enter ur age:"))

    def greet(self):
        print(f"Hello,my nsme is{self.name} and i am {self.age} years old.")

person1 = person()


person1.greet()

                                        


