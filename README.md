# Object-Oriented-Programmig

## OOP in Python 

**This part contains notes from "CS50P - Lecture 8 - Object-Oriented Programming" Youtube video which is all about OOP in Python.**

- OOP is a pretty compelling solution to problems that you invariably encounter as your programs get longer, larger and more compliacted. 

### student.py

#### Tuples

- When would you use a tuple versus a list? -> When you want to program defensively, or, in general when you know that the values in this variable shouldn't change, so why would you use a data type that allows them to be changed? It just invites mistakes, bugs down the line, either by you or colleagues who are interacting with your code. So tuple is just another way where you can increase the probablitiy of correctness by just not letting anyone, yourself included, change the contents there in. 


**Immutable:** means that you cannot change the value

    def main():
			student = get_student()
			if student[0] == "Padma"
				student[1] = "Ravenclaw"
			print(f"{student[0]} from {student[1]}) 

		def get_student(): 
			name : input('Name: ')
			house : input('House: ')
			return (name, house) 

	name : "Padma"
	house : "Gryffindor"

- We just see a big mess of error which is a "TypeError": 'tuple' object does not support item assignment. --> Here is a manifestation of the immutability of tuples. You cannot change location 0 or 1 or anything inside, That is a feature. That is the design of the tuple

- We can do nested tuples as well as doing nested list. 

#### Dictionaries

- Dictionary is a little more powerful in that you can semantically associate keys, little descriptions, with the values, those keys and those values, respectively.

- Dictionaries are **mutable.**

    def main():
		student = get_student()
		if student['name'] == "Padma"
			student['house'] = "Ravenclaw"
		print(f"{student['name']} from {student['house']}) 

	def get_student():
		student = {} 
		student["name"] = input("Name: ")
		student["house"] = input ('House: ')
		return student

#### Classes

- A class is like a blueprint for pieces of data objects, is like a mold that you can define and give a name and when you use that mold or use that blueprint you get types of data that are designed exactly as you want. So in short, classes allow us to invent our own data types in Python and give them a name. This is a primary feature of OOP to be able to create our own objects in this way and, in the case of Python in classes, even give them some custom names.

    class Student //we define class which is our own data 'type'
			...

	def main():
		student = get_student() 
		print(f"{student.name} from {student.house}) 

	def get_student():
		student= Student() //Creating object of that class
		student.name = input("Name: ")
		student.house = input("House: ")
		return student

!!! Now what's really powerufl about class and OOP  more generally, is that we have created this custom data type called 'Student'. We have stored one such 'student' in a variable like we can always do in a variable called 'student'- We can call it anything we want- and then we are returning that variable "student.name = input("Name: ") student.house = input("House: ")" that has the result of putting inside of that class, a name 'attribute ' and a house 'attribute'. 

**Objects**

- It turns out that we can create a class, using that class keyword. But anytime we use a class, we are creating what are called objects. We have instances of classed with objects.

- !Classes are mutable but we can make them immutable.

#### Instance Methods

- In the context of classes, there are a number of not just attributes or instance variables that you can put inside, but also 'methods'. Classes come with certain methods, or functions inside of them that you can define, and they just behave in  a special way. These funtions allow you to determine behaviour in a standart way

    class Student:
        def __init__(self,name, house) //This is designed by the authors of Python and if we want to initialize the contents of an object from a class, we define this method, and we'll see what it's about to do here.
            self.name = name// storing them in really, identically
            self.house.house// named 'instace variables' in the object

    def main():
        student = get_student()		 
        print(f"{student.name} from {student.house}") 

    def get_student():	
        name = input("Name: ")
        house = input("House: ")
        student  = Student(name,house) //This line is constructor.  
        return student


- **What is differance between init method and default constructor?->** In other languages, for instance Java, there are functions that are explicitly called constructors that contruct an object,they initialize it with values.Python technically calls this init method the initializition method, it initalizes the value.

- **What about if you want to store more than one name or more?->** Instead of self.name1, self.name2 we can use sefl.names = [] but not for this case, maybe another ones.

- **How are classes and objects represents in memory? ->** The class is technically just code that defines that blueprint.Objects are stored in the computer's memory by taking up some number of bytes. Python, the interpreter, handles those lower level details for us. 

- **If we can do the same thing with the dictionaries, so why we use classes ? ->** In short explanation; you can do much more with classes. You can ensure the correctness of your data much more with classes. You can error-check things. And generally you can design more complicated software more effectively. 

-Classes, OOP more generally encourages you to encapsulate, inside of a class, all functionality related to that class. So if you wanna validate the name or the house is correct, that belongs just fundamentally in the class called student itself, not in some random function that you wrote elsewhere

**Raise :** It turns out, in Python, there is another keyword related to exceptions that Python itsel uses to raise all of those exceptions we've talked about in the past. When you caught things like values errors or other such exceptions that come with Python, it turns out you, the programmer can raise that is create your own exceptions when sth just really goes wrong; not wrong enough that you want to quit and exit the whole program, but enough that you need to somehow alert the programmer that there has been an error.

		class Student:
			def __init__(self,name, house) 
				if not name : 
					raise ValueError("Missing name")
				if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
					raise ValueError("Invalid house")
				self.name = name
				self.house.house

		def main():
				student = get_student()
				print(f"{student.name} from {student.house}) 

			def get_student():	
				name = input("Name: ")
				house = input("House: ")
				return Student(name,house) 

**__str__ ->** There are other special methods in Python when it comes to classes; not just __init__ ,but continuining in the same pattern __str__. If you define it inside of your class, Python will just authomatically call this function for you anytime some other function wants to see your object as a string. Print wants to see your object as a string. 

        class Student:
			def __init__(self,name, house) 
				if not name : 
					raise ValueError("Missing name")
				if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
					raise ValueError("Invalid house")
				self.name = name
				self.house.house

			def __str__(self)
				return f"{self.name} from {self.house}"

		def main():
				student = get_student()
				print(f"{student.name} from {student.house}) 

		def get_student():	
			name = input("Name: ")
			house = input("House: ")
			return Student(name,house) 

- !What's powerful about classes unlike dictionaries alone,is that classes can have , not just variables or instance variables those attributes we keep creating. They can also have functions built in, a.k.a methods. When a function is inside of a class, it's called a "method" but it's just a function. 

**Another Feature :** properties -> Property is just an attribute that has even more defense mechanisms put into place, a little more functionality implemented by you to prevent programmers, from messing things up like these attributes. So again; a property is going to be an attribute that we have more control over. -> @property , which is technically a function.

	class Student:
		def __init__(self,name, house) 
			
			self.name = name
			self.house= house 

		def __str__(self)
			return f"{self.name} from {self.house}"

		# Getter // getter is a function for a class that gets some attributes 
		@property
		def house(self):
			return self._house//we should have house name for variable or function name because they gonna collide

		# Setter // setter is a function in some class that sets some value
		@house.setter
		def house(self,house):
			if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
				raise ValueError("Invalid house")
			self._house = house

		@property
		def name(self):
			return self._name	

		@name.setter
		def name(self,name):
			if not name:
				raise ValueError("Missing name")
			self_name =name


	def main():
		student = get_student()
		print(f"{student.name} from {student.house}) 

	def get_student():	
		name = input("Name: ")
		house = input("House: ")
		return Student(name,house)


### hat.py

- !!!When should we use a class to represent something in our code? -> Very often , when we are trying to represent some real world entity or fantasy world entity, like a student ,which is something in the real world.

### wizard.py

#### Inheritance

- !!! Object-oriented programming offers a solution.It turns out that object-oriented programming in Python also supports inheritance, whereby you can define multiple classes that somehow relate to another.They dont need to exist in parallel in this way. There could actually be some hierarchy between them. 

- If you were to have a super superclass, so your hierarchy is even taller than the two levels of hierarcy that we currently have, you actually do inherit all of the functionality, not just from one level above you but from two or three, so you can indeed access some of that functionality as well. 