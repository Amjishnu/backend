a=[1234,"jishnu",4.12,True] #ordered,allow duplicates, changable, allows multitype
print(type(a)) #list
print(len(a)) #list length
print(a[3]) #list position

print(a[1:3]) #list slicing
print(a[-3:-1]) # reverse slicing
print(a[:2]) #last to first positon
print(a[2:]) #first to last positon

a[1] ="RDJ" #replacing values
print(a)

a.insert(2,"sss") #inserting extra value by replacing using index
print(a)

a.append("bbb") #adding an extra value in the end 
print(a)

b = [2,3,4,5] #extending another list "b" in to 'a' using extend
a.extend(b)
print(a)

c = ('jishnu','vishnu')
a.extend(c) # extending a tuple
print(a)

a.remove("jishnu") #removing an element
print(a)
  
a.remove(4.12)
print(a)
 
a.pop()
print(a) #pop to remove the last element

a.pop(2) #to remove value from a specific index
print(a)

del a[3]
print(a)