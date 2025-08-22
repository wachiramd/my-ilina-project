class Animal:
	def __init__(self,name, age):
		self.name = name
		self.age = age

	def sound(self):
		print("The dog's name is {} and the age is {}".format(self.name, self.age))

sule = Animal("Sule", 12)
sule.sound()

class Dog(Animal):
	def __init__(self, fur):
		self.fur = fur
dule = Dog("Dule", 13)
dule.Dog()
isinstance(fur, Dog)
