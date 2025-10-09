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
    'Year':2029

}
Studentinfo.pop('Shanto')
print(Studentinfo)
Studentinfo.popitem()  # Remove the last item from the dictionary
print(Studentinfo)

