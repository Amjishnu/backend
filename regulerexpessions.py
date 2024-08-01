


import re

txt="steve Roger is captain America"
x=re.search("^steve.*America$",txt)

if x:
    print("we have a match")
else:
    print("we don't have a match")
    # the findall()function return a list containing all matchs

y=re.findall("[a,m]",txt)
print('a,m,y')
# find all lower case charecters "a"and "m" with the given string

txt1="Iron Man's latest armour is mark 44"
z=re.findall("\d",txt1)
print('digits',z)
# find all digits charecters

a=re.findall("latest|oldest",txt1)
print('or',a)
# check if the string containg either "falls" or "stays"
if a:

    print("correct")
else:
    print("not correct")

b=re.findall("\D",txt1)
print('non digits',b)
# return a match at every non-digit charectores
if b:
    print("correct")
else:
    print("not correct")

c=re.findall("\S",txt1)
print('white space',c)

if c:
    print("correct")
else:
    print("not correct")
#     # return match at every non white space characters

e=re.findall("\w",txt1)
print('word',e)

if e:
    print("correct")
else:
    print("not correct")

f=re.findall("\W",txt1)
print('non words',f)

if f:
    print("correct")
else:
    print("not correct")

g=re.findall("\AIron",txt1)
print('starts',g)

if g:
    print("correct")
else:
    print("not correct")


h=re.findall("[a-n]",txt1)
print('between a and n:',h)

if h:
    print("correct")
else:
    print("not correct")


i=re.findall("[a,r,n]",txt1)
print('string as any a,r,or n:',i)

if i:
    print("correct")
else:
    print("not correct")

j=re.findall("[^a,r,n]",txt1)
print('srting has others charecters than a,r,or n:',j)

if j:
    print("correct")
else:
    print("not correct")

k=re.findall("[0,1,2,4,5]",txt1)
print('stings has any 0,1,3,4,5 digits:',k)

if k:
    print("correct")
else:
    print("not correct")

m=re.findall("[0-5][0-9]",txt1)
print('string has any two digits numbers,from 00 to 59',m)

if m:
    print("correct")
else:
    print("not correct")


n=re.findall("[a-zA-Z]",txt1)
print('string has any characters from a to z lowers case, and z to upper case:',n)

if n:
    print("correct")
else:
    print("not correct")

o=re.split("\s",txt1)
print("split the string at every white space characters",o)

p=re.split("\S",txt1,1)
print('split the string at the first white space characters:',p)

q=re.sub("\s","9",txt1)
print('replace all white space characters with the digit "9":',q)













