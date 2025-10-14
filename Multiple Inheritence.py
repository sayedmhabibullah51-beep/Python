class Baba:
    Car='BMW'
    Money='1000 Crore'
    Bari='Tajmahal'

class Baba2:
    Laptop='Doell'
    Smartphone='Iphone'
    Webcam='Sony'

class Baba3:
    Gym='Oxfoard Mission Road'
    AC='Walton'
    Camera='Casio'

class kaka(Baba,Baba2,Baba3):
   Kissunai=''
   Vadaima=''

k= kaka()
print(k.Car)
print(k.Smartphone)
print(k.AC)
print(k.Gym)
print(k.Money)
print(k.Laptop)
print(k.Webcam)
print(k.Bari)
print(k.Camera)