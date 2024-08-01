a={3,1,4,2,10}
print(a)


a.add(5)
print(a)

b={5,6,7}
a.update(b)
print(a)

a.remove(5)
print(a)

a.discard(3)
print(a)

c={9,8,10}
d=a.union(c)
print(a)
 
e={4,7,9,10,11,25}
f=a.intersection(e)
print(f)

