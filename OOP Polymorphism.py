class Car():
    def __init__(self,name,model,component,speed,color):
        self.name = name
        self.model= model
        self.speed=speed
        self.color=color
class My(Car):
    pass
p= Car('RRR','r1234','varios','600000hp','Crimson')
print(p.color)
print(p.speed)

class Mobile():
    def __init__(self,Model,Camera,Storage,Color):
        self.Model=Model
        self.Camera=Camera
        self.Storage=Storage
        self.Color=Color
class My(Mobile):
    pass
class Brother(Mobile):
    pass
class Father(Mobile):
    pass

m=Mobile('Iphone','600px','128gb','Crimson')
b=Mobile('Samsung','765px','124gb','Blue')
f=Mobile('Nokia','845px','545gb','Purple')
print(m.Color,m.Model,m.Camera,m.Storage)
print(b.Color,b.Model,b.Camera,b.Storage)
print(f.Color,f.Model,f.Camera,f.Storage)

class Fruit():
    def __init__(self,name,color,size,smell):
        self.name=name
        self.color=color
        self.size=size
        self.smell=smell
class My(Fruit):
    pass
class Brother(Fruit):
    pass
class Mother(Fruit):
    pass
m=Fruit('Mango','Yolloish','Big','Trimindios')
b=Fruit('Banana','Yellow','Gigentic','Or Bou jany')
M=Fruit('Cherrie','Red','Medium','Light sweet')
print(m.name,m.color,m.size,m.smell)
print(b.name,b.color,b.size,b.smell)
print(M.name,M.color,M.size,M.smell)


class Watch():
    def __init__(self,name,color,style):
        self.name=name
        self.color=color
        self.style=style
class My(Watch):
    pass
class Borovai(Watch):
    pass
class Janina(Watch):
    pass
m=Watch('Timezone','Blue','vintage')
b=Watch('Rolex','Golden','Classic')
j=Watch('Timewatch','Silver','Bold')
print(m.name,m.color,m.style)
print(b.name,b.color,b.style)
print(j.name,j.color,j.style)