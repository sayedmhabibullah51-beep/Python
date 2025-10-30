File=open('Shanto.text','a') # a use korle koi bar print korsi tao dakhabey
File=open('Shanto.text','w')

File.write(' My name is Shanto \n')
File.write('I am from Barishal \n')
File.write('I like Hotch Potch \n')
File.write('I like MMA')


File=open('Shanto.text','r')
print(File.read())
