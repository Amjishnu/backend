import datetime

x=datetime.datetime.now()
print(x)
# the datetime object has a method for formatting data object into readable string
# return year
print(x.year)
print(x.strftime("%A"))
# return weekday name

a=datetime.datetime(2020,10,28)
print(a.year)
print(a.strftime("%B")) #guess and returns month

# guess and returns day
print(a.strftime("%A"))  