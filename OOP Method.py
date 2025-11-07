# Instance Method

class Bank():
    def Instancemethod(self):
        print('This is a book')
b=Bank()
b.Instancemethod()

# CLASS METHOD
class School():
    @classmethod
    def Headmaster(cls):
        print('This is my school')
School().Headmaster()    # CLASS METHOD AY VERIABLE DICLARE KORA LAGEY NA

# STATICS METHOD

class Hospital():
    @staticmethod
    def Doctor():           # STATIC METHOD AY PERAMITER LAGEY NA
        print('This a Patient')
Hospital().Doctor()

# EXERCISE

class Myname():
    def InstanceMethod(self):
        print('Hello Instance Method')

    @classmethod
    def ClassMethod(cls):
        print("Hello Class Method")
    @staticmethod
    def StaticMethod():
        print('Hello Static Method')

Myname().InstanceMethod()  # AYKHANEY RUN HOISEY KARON AYTAY CLASS METHOD ROISEY NA HOILEY VERIABLE LAGTO
Myname().ClassMethod()
Myname.StaticMethod()








