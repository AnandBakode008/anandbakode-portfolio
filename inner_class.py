#outer Class
class Car:

	#Constructor 
	def __init__(self):
		print("Car Is a Outer class ")

    # inner  Class
	class Engine:
		def __init__(self):
			print("Engine is a Inner Class")


#object Creation 
car=Car()

#Object Creation 

b=Car.Engine()