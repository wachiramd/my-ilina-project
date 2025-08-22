class Dog:
	species = "mammal"

	def __init__(self, name, age):
		self.name = name
		self.age = age

philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
bosco = Dog("Bosco", 1)

philo.age = 7
bosco.species = "fish"

print("what is the name of your dog?")
y_name = input()
print("what is the age of your dog?")
y_age = int(input())

print("{} is {} and {} is {} and then there is {} who is {}".format(philo.name, philo.age, mikey.name, mikey.age, bosco.name, bosco.age))
print("Your dog's name is {} of {} years".format(y_name, y_age))

if bosco.species == "mammal":
	print("{} is a {}".format(bosco.name, bosco.species))
else:
	print("{} is a {}".format(bosco.name, bosco.species))

