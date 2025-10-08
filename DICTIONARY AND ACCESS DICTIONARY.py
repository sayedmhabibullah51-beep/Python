Studentinfo={
    'Shanto':{
        'Address':'Oxford Mission Road',
        'Home Name':'Mira bari',
        'Number':123485994,
        'House Number':4948,
    },
    'Rayhan':{
        'Address': 'Oxford Mission Road, Diya bari',
        'Home Name': 'Mira bari,9988',
        'Number': 12348599959684,
        'House Number': 49585848,


    },


    'Year':2018
}
print(Studentinfo['Rayhan']['Number'])

# ACCES DICTIONAR:
#keys
c= Studentinfo.keys() # keys dara only Main key (Shanto,Rayhan,Year) agulo dakhabey
print(c)

#values
d=Studentinfo.values() #Values dara only Nested Key dakhabey Value akarey Main key dakhabey na
print(d)


f={1:'Welcome', 2:'to', 3:'the', 4:'jungle'}
print(f)
