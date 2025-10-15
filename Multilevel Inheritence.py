class Baba:
    Car='BMW'
    Money='1000 Crore'
    Bari='Tajmahal'

class Son1(Baba):
    Laptop='Doell'
    Smartphone='Iphone'
    Webcam='Sony'

class Son2(Son1):
    Gym='Oxfoard Mission Road'
    AC='Walton'
    Camera='Casio'

class Son3(Son2):
   Kissunai=''
   Vadaima=''

b=Son1()
m=Son2()
c=Son3()
print(b.Car)
print(m.Smartphone)
print(c.Bari)
print(c.Webcam)
print(c.AC)