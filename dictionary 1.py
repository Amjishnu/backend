a={"Brand" : "ford", "model": "mustang", "year":2024 }
print(a)

#above given 2 ways of representing dictionaries

x=a.get("model") #displays the item in given label
print(x)

y=a.keys() # display the labels of the given dictionary
print(y)

z=a.values() #display the values/ items of the given dictionary
print(y)

t=a.items() #crossponding values/items
print(t)

a.update({"model" : "renault"})
print(a)

a["Type"] ="racing"  #addiong extra label and value
print(a)

a["colour"] =["matte navy bule ","matte black"] #any datatypes can be added into the dictionaries
print(a)