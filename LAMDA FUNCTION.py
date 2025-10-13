def addition(a,b,d):
    sum =a+b+d
    print(sum)
addition(10,20,4)


# LAMDA is a way to create small anonymous functions in Python.

x= lambda a,b,c:a+b+c  # It uses the syntax: lambda arguments: expression.
print(x(10,20,4))
x= lambda x,y,z:x*y*z
print(x(4,5,6))
v= lambda m,n,b,g,j:(m-n-b)*(g/j)
print(v(66,77,88,99,988))
m=lambda q,w,e,r,t,y:(q+w+e)*(r*t/y)
print(m(22,33,44,55,66,67))