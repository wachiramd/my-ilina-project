#Sorting lists
#sort the names-start with surnames

hnames = ['Michael Collins','Daniel Wachira','Stuart Russel', \
	'Dwarkesh Patel','Mo Gawdat','Sienka Dounia','Miles Brundage']
print(hnames)
hnames.sort()
print(hnames)
hnames.sort(key = lambda x: x.split()[1])
print(hnames)

people = [('Daniel', 35), ('Wachira', 25), ('Jerad', 88), ('EsqMD', 30)]
print(people)
people.sort(key=lambda x: x[1])
print(people)

#Sorting a list of Objects - OOP
print("from here we are dealing with objects")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'{self.name}: {self.age}'

daniel = Person('Daniel', 35)
wachira = Person('Wachira', 25)
jerad = Person('Jerad', 99)
esq = Person('EsqMD', 30)
p = [daniel,wachira,jerad,esq]
print(p)
p.sort(key = lambda x:x.age)
print(p)


