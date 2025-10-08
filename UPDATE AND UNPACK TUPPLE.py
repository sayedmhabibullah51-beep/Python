ThisTuple=('aat','aa3e','hfj','uru','fifii')
a=list(ThisTuple)
print(type(list(ThisTuple)))
print(type(a))
a.append('sss')
print(a)
b=tuple(a)
print(b)

#UNPACK TUPLE
fruite=('apple','banana','cherrie','iiij','gthh','jrjgrkjg','fhruhr')
(a,b,*c) = fruite
print(c)