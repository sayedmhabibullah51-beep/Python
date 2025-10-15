Fruits=[1,2,3,4,5,6,7,8,9,10]
for x in range(len(Fruits)): # range(len()) Ayta use korsi index dakhar jonno
    if x==5:
        break
    print(x)

Name = ['Shanto', 'Prodip', 'Pranto', 'Apple', 'Avocado', 'Strawbery']
for i in Name:
    if i=='Apple':
        break
    print(i)

Name=['Shanto', 'Prodip', 'Pranto', 'Apple', 'Avocado', 'Strawbery']
for b in Name:
    if b=='Apple':
        continue
    print(b)