x=open("greetings.txt","rt")
print(x.read())
x.close()

x=open("greetings.txt","w")
x.write("hello")
x.close()

x=open("greetings.txt","rt")
print(x.read())
x.close()





