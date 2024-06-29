a={"Brand": "ford", "model" :"mustang", "year" :1947}
print(a)

if "model" in a:
    print("yes model presentin the key lists")

a["year"] = 1980 #updating without update()
print(a)

a.update({"type" : "racing"}) #adding new elements using update()
print(a)

a["colour"] = ["matte navy blue","matte black"] #any datatypes can be added in to the dictionarys
print(a)

a.pop("type") #we can decide with element should be poped or deleted
print(a)

a.popitem() #automatically the last item will be deleted
print(a)

del a["year"]
print(a)

a.clear()
print(a)
