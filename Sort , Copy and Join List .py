#ASSENDING ORDER OR ALAIGN
number=[3,4,5,7,60,1,7,4,2]
fruite=['orrange','lichi','banana','alu'] #ALPAHBET AKAREY CHANGE KOBE
fruite.sort()
number.sort()
print(fruite)
print(number)

#REVERSE
num=[1,2,3,4,5,6,7,8,9]
alph=['a','b','c','d','e','f']
alph.sort(reverse= True)
num.sort(reverse = True)
print(alph)
print(num)

#COPY LIST
numbe=[11,22,33,44,55,66,77]
num1=numbe.copy()
print(numbe)
print(num1)

#JOIN LIST
c=['a','b','v','s']
d=[12,3,4,4]
e=c+d
c.extend(d)
print(c)