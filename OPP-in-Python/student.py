# name : input('Name: ')
# house : input ('House: ')
# print(f"{name} from {house})
	

# def main():
# 	name = get_name()
# 	house = get_house()
# 	print(f"{name} from {house}")

# def get_name(): 
# 	name : input('Name: ')
# 	return name

# def get_house(): 
# 	house : input('House: ')
# 	return house

# if __name__ == "__main__":
# 	main()

# def main():
# 	student = get_student()
# 	#//unpack of those name and house values in two separate variables
# 	print(f"{student[0]} from {student[1]}") 

# def get_student(): 
# 	name : input('Name: ')
# 	house : input('House: ')
# 	#//I minimally like to return both of those but how?
# 	return (name, house) #// tuple : Type of data in Python, collection of values, immutable

# def main():
# 	student = get_student()
# 	if student[0] == "Padma":
# 		student[1] = "Ravenclaw"
# 	print(f"{student[0]} from {student[1]}") 

# def get_student(): 
# 	name : input('Name: ')
# 	house : input('House: ')
# 	return (name, house) 

# name : "Padma"
# house : "Gryffindor"

# def main():
# 	student = get_student()
# 	if student[0] == "Padma":
# 		student[1] = "Ravenclaw"
# 	print(f"{student[0]} from {student[1]}") 

# def get_student(): 
# 	name : input('Name: ')
# 	house : input('House: ')
# 	return [name, house] #// As we used square brackets, this is indeed explicitly a list and it is 'MUTABLE' - that is to say that you can change the contents of a list.

# def main():
# 	student = get_student()
				
# 	print(f"{student['name']} from {student['house']}") 

# def get_student():
# 	student = {} 
# 	student["name"] = input("Name: ")
# 	student["house"] = input ('House: ')
# 	return student

# def main():
# 	student = get_student()
# 	if student['name'] == "Padma":
# 		student['house'] = "Ravenclaw"
# 	print(f"{student['name']} from {student['house']}") 

# def get_student():
# 	student = {} 
# 	student["name"] = input("Name: ")
# 	student["house"] = input ('House: ')
# 	return student

# class Student #//we define class which is our own data 'type'
# 	...

# def main():
# 	student = get_student()	 
# 	print(f"{student.name} from {student.house}") 

# def get_student():
# 	student= Student() #//Creating object of that class
# 	student.name = input("Name: ")
# 	student.house = input("House: ")
# 	return student

# class Student:
# 	def __init__(self,name, house) #//This is designed by the authors of Python and if we want to initialize the contents of an object from a class, we define this method, and we'll see what it's about to do here.
# 		self.name = name  #// storing them in really, identically
# 		self.house.house  #// named 'instace variables' in the object

# def main():
# 	student = get_student()			 
# 	print(f"{student.name} from {student.house}") 

# def get_student():	
# 	name = input("Name: ")
# 	house = input("House: ")
# 	student  = Student(name,house) #//This line is constructor.  
# 	return student

# class Student:
# 	def __init__(self,name, house):
# 		if not name : 
# 			raise ValueError("Missing name")
# 		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
# 			raise ValueError("Invalid house")
# 		self.name = name
# 		self.house.house		

# def main():
# 	student = get_student()
# 	print(f"{student.name} from {student.house}") 

# def get_student():	
# 	name = input("Name: ")
# 	house = input("House: ")
# 	return Student(name,house)

# class Student:
#     def __init__(self,name, house):
#         if not name : 
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house.house

#         def __str__(self):
#             return f"{self.name} from {self.house}"

# def main():
# 	student = get_student()
# 	print(f"{student.name} from {student.house}") 

# def get_student():	
# 	name = input("Name: ")
# 	house = input("House: ")
# 	return Student(name,house) 


# class Student:
# 	def __init__(self,name, house,patronus):
# 	    if not name: 
# 			raise ValueError("Missing name")
		
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
# 			raise ValueError("Invalid house")
		
#         self.name = name
# 		self.house=house
# 		self.patronus = patronus

# 	def __str__(self):
# 		return f"{self.name} from {self.house}"

# 	def charm(self): 
# 		match self.patronus: 
# 			case "Stag": 
# 				return "stag"
# 			case "Otter": 
# 				return "otter"
# 			case "Jack Russell terrier"
# 				return "dog"
# 			case _:
# 				return "wand"

# def main():
# 	student = get_student()
# 	print("Expecto Patronum!")	
# 	print(student.charm()) 

# def get_student():	
# 	name = input("Name: ")
# 	house = input("House: ")
# 	patronus = input("Patronus: ")
# 	return Student(name,house,patronus)

# class Student:
# 	def __init__(self,name, house):		
# 		self.name = name
# 		self.house= house 

# 	def __str__(self):
# 		return f"{self.name} from {self.house}"

# 	# Getter // getter is a function for a class that gets some attributes 
# 	@property
# 	def house(self):
# 		return self._house #//we should have house name for variable or function name because they gonna collide

# 	# Setter // setter is a function in some class that sets some value
# 	@house.setter
# 	def house(self,house):
# 		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
# 			raise ValueError("Invalid house")
# 		self._house = house

# 	@property
# 	def name(self):
# 		return self._name	

# 	@name.setter
# 	def name(self,name):
# 		if not name:
# 			raise ValueError("Missing name")
# 		self_name =name


# def main():
# 	student = get_student()
# 	print(f"{student.name} from {student.house}") 

# def get_student():	
# 	name = input("Name: ")
# 	house = input("House: ")
# 	return Student(name,house)


# class Student:
#     def __init__(self,name, house):		
# 	    self.name = name
# 	    self.house= house 

# 	def __str__(self):
# 	    return f"{self.name} from {self.house}"

#     @classmethod
#     def get(cls):	
#         name = input("Name: ")
#         house = input("House: ")
#         return cls(name,house)

# def main():
# 	student = Student.get()
# 	print(student) 

# if __name__ == "__main__":
#  	main()