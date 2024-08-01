class animal:
    def speak(self):
        pass

class dog(animal):
    def speak(self):
        return "woof"
    
class cat(animal):
    def speak(self):
        return "meow"
    
class duck(animal):
    def speak(self):
        return ("quick")
    

dog = dog()
cat = cat()
duck = duck()

print(dog.speak())
print(cat.speak())
print(duck.speak())