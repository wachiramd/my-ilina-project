class Person:
	description = "general person"

	def __init__(self, name, age, origin):
		self.name = name
		self.age = age
		self.origin = origin

	def speak(self):
		print("My name is {}, I'm {} years old and I am from {}".format(self.name, self.age, self.origin))
	def eat(self, food):
		print("{} eats {}".format(self.name, food))
	def action(self):
		print("{} jumps".format(self.name))

#Now we introduce the child class

class Baby(Person): #Person in the brackets 
	description = "I am just a baby"
	def speak(self):
		print("I am a baby, I do not speak at all") #This attribute is unique to the baby class alone
	def nap(self):
		print("{} takes a nap".format(self.name)) #This takes an attribute from the Person class


person = Person("Steve", 20, "China")
person.speak()
person.eat("Pasta")
person.action()


baby = Baby("Ian", 2, "Kenya")
baby.speak()
baby.eat("Milk")
baby.action()

'''print(person.description)
print(baby.description)
'''

print(isinstance(baby, Person))
print(isinstance(baby, object))
