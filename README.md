# __O__ bject __O__ riented __P__ rogramming (OOP) 
A programming paradigm that organizes data and behavior into reusable and self-contained __objects__. These __objects__ contain both data (__attributes__ or __properties__) and __methods__ (functions or procedures) that operate on the data. 
__The primary purpose of OOP is to increase the reusability and maintainability of code.__

## Benefits of OOP:

- **Modularity:** 
	OOP promotes modularity by encapsulating the implementation details within objects, making it easier to understand and use.
- **Reusability:** 
	Objects and classes can be reused in different parts of the program or in different programs, reducing development time and effort.
- **Maintainability:** 
	OOP code is easier to maintain and modify, as changes to one part of the system do not affect other parts as long as the interface remains unchanged.
- **Flexibility and Scalability:** 
	OOP provides a flexible and scalable way to design and develop complex applications.

We’ve been using OOP with any built in methods we use (range(), len(), append(), print(), type())
print(type('Hello')) → <class 'str'>
Each type of thing, or __object__, has specific properties and functionality associated with it. Thats why we cant concatenate an int with a string etc (TypeErrors )

This grouping, or *encapsulation*, of properties and functionalities by object is a fundamental principle of OOP and is implemented with classes.
## Classes and Objects
[Classes - Platform](https://login.codingdojo.com/m/506/12458/87321)
### Class:
#### IS
- A class is a blueprint or a template for creating objects. It defines the properties (attributes) and methods (functions) that the objects of the class will have.
- By defining a class, in effect we've defined a new data type!
#### DOES
- Sanitizes available data to your applications needs(Not all users are the same for all apps)
	- Represents what each INSTANCE of an object will look like
	(All users have the same attributes but my info is different than yours)
### Object: 
#### IS
- An object is a real-world entity that is an instance of a class. It is a basic unit of Object-Oriented Programming and represents a unique occurrence of a class.
- **Conceptually, objects are like the components of a system.**
#### DOES
- Will end up being each row of a DB 
### `class` Syntax
- `class`
All class definitions start with the class keyword, which is followed by the name of the class and a colon
- `class Name` - capitalized and singular
```python
class User:
	pass
	# Class Attributes/Properties/DATA
	
	# Constructor Method
	    # Instance Properties/Attributes/DATA
	
	# Methods/functions/ACTIONS
```

## Constructor
[Constructor - Platform](https://login.codingdojo.com/m/506/12458/87322)
```python
class User:
	# Class Attributes/Properties/DATA
	def __init__(self): #Constructor Method
		# Properties/Attributes/DATA
```
- `__init__()` is a reserved method in python classes
- [[self]] 
	- represents the instance of the class (`this` in js)
	- allows methods to operate on the object's data and behavior, enabling the creation of dynamic, reusable, and object-specific code within classes.
- You can give `__init__()` any number of parameters
	- The first parameter will always be a variable called `self`. 
	- When a new class instance is created, the instance is automatically passed to the self parameter
- `__init__()` sets the initial state of the object by assigning the values of the object’s properties

```python
class User:
	# Class Attributes/Properties/DATA
	def __init__(self): #Constructor Method
		# Properties/Attributes/DATA
		self.first_name = 'Cameron'
		self.last_name = 'Smith'
		self.email = 'cs@email.com'
		self.age = 34
		self.has_kids = True
		self.children = ['Harper', 'Walter']
```
- `user1 = User()` This calls the `__init()__`constructor and creates a __class object__ in memory
```python
print(user1)
# <__main__.User object at 0x0000016B7740F9D0>
```
This print() indicates where the object is stored in your computer’s memory. 
- `__main__` is the name of the module where the `User` class is defined. If the class was defined in a different module, that module's name would be displayed instead of `__main__`. 
- `User` is the name of the class to which the object belongs.
- `0x0000016B7740F9D0`: This is the memory address of the object in hexadecimal format. It uniquely identifies the location in the computer's memory where the object's data is stored. 
- Every object has a different memory address. Note that the address you see on your screen will be different and mine changes each time AREPL runs the file.

## Attributes
**What do classes HAVE**
### (Instance )Variables/Attributes
- Defined in the `__init__()` method
- An instance attribute’s value is specific to a particular instance of the class. 
(*All User objects have a name and an age, but the values for the name and age attributes will vary depending on the User instance.*)
- Characteristics shared by all instances of the class type
==**We don't want all our users to be me**==
```python
class User:
    def __init__(self, first, last, email, age, kids = False):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
        self.has_kids = kids
        self.children_names = []

user1 = User('Cameron', 'Smith', 'cs@email.com', 34, True)
```
#### Accessing/Updating Attributes (Directly)
```python
print(user1.email)
user1.first_name = "Jeffrey"
user1.children = ['Harper', 'Walter']
print(user1.first_name)
print(user1.children)
```
### (Class) Variables/Attributes
define a class attribute by assigning a value to a variable name 
__outside__ the `__init__()` __inside__ the class
```python
class User:
    species = "Homo sapien"
    total = 0
print(User.species)
```
## Methods
[Methods - Platform](https://login.codingdojo.com/m/506/12458/87323)
**What classes DO** or **Actions that an object can perform**
### (Instance ) Functions/Methods
==Initially set up  without passing self as a method parameter==
```python
def birthday():
  #Increases Age
  pass
def greeting():
  #say Hello
  print("Hello")
def name_children():
  pass

user1.greeting()
```
*TypeError: User.greeting() takes 0 positional arguments but 1 was given*
We are calling on the method from the instance, this is known as implicit passage of self

When we call a method from an instance, the memory address of that instance, along with all of its information (name, email etc…), is passed in as `self`
## `self`
### Definition
`self` is a reference to the instance of the class
`self` allows methods to operate on the object's data and behavior, enabling the creation of dynamic, reusable, and object-specific code within classes.
### Initializer (`__init__`) Method:

The `__init__` method is a special method in Python classes that is automatically called when a new instance of the class is created. It initializes the object's attributes. `self` is used to refer to the instance being created, allowing you to set its initial state

(*This parameter is named `self` by convention, though you could technically name it something else (although it's highly discouraged due to conventions and readability).*)

```python
class MyClass:
    def __init__(self, value):
        self.value = value
```
## Instance Methods:
In Python, When you create an instance of a class (an object), and you call a method on that object, Python automatically determines which object the method is associated with and passes it as the first parameter to the method
- name the first parameter of instance methods in a class as `self`
methods defined inside a class can access and modify object attributes or to operate on the object's attributes and behavior
```python
    def print_value(self):
        print(self.value)
	
	def double_value(self): 
		self.value *= 2

# Creating an instance of MyClass
obj = MyClass(42)

# Calling an instance method on the object
obj.print_value()  # Output: 42
obj.double_value()
print(obj.value) # Output: 84
```
In the `print_value` method, `self` refers to the specific instance of `MyClass` (`obj` in this case) on which the method is called. When you call `obj.print_value()`, `self` inside the `print_value` method is automatically set to `obj`.


#### Accessing/Updating Attributes (via built-in reusable methods)
```python
	def greeting(self):
        print(f"Hello, my name is {self.first_name}")
        return self
	
    def birthday(self):
        self.age += 1
        return self
	
    def name_children(self, child_name):
        self.children.append(child_name)
        return self
```
## Chaining
Each class method should `return self`
Then it is accessible as an implied argument for each chained method call
```python
user1.name_children("Charlotte").birthday().repr()
```
## `__repr__()`
[repr() - DOCS](https://docs.python.org/3/reference/datamodel.html#object.__repr__)
The `__repr__` method is used to define the "formal" or unambiguous string representation of an object.
(*It is meant to return a string that, if passed to the Python interpreter, would create an object with the same state as the current object, it should ideally be a valid Python expression.*)
```python
class Book:
	def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

	def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)
print("Using repr(): ", repr(book1))
# Output: Book('The Hitchhiker's Guide to the Galaxy', 'Douglas Adams', 224)
```
- Debugging tools like IDEs or the Python interactive interpreter often use the `__repr__` method to display object information when inspecting variables.
- Python built-in functions like `repr()` directly call the `__repr__` method of an object.
- By using `__repr__`, you adhere to a convention that other developers familiar with Python will recognize. It's a standard way to represent objects
## OOP & Dictionaries
[OOP & Dictionaries](https://login.codingdojo.com/m/506/12458/90791)
Why use classes instead of dictionaries or lists or both?
- By creating classes out of our mostly useless raw data we now have access to all the associated attributes/methods of that class/instance
- Its less memory 
```python
import sys
for thing in pretendDB.people:
    print(sys.getsizeof(thing))
    print(sys.getsizeof(User(thing)))
```
- Lists of dictionaries is how or db will be returning table info to us in flask with pymysql/mysql
- Something you will see a lot as a programmer is that key-value pair structures 
	- often used for data coming from other sources, even from external programs written in different languages, typically in the form of JSON through an API
- Also called:
	- Hash-table(C#), 
	- Maps, Hash Map(Java, C++), 
	- Objects(JavaScript, JSON) 
	- Associative Array (PHP) etc…

We Can Refactor our `__init__` constructor to accept a dictionary as input
```python
# from dir import file
from pretendDBresponse import people
# print(people)

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.age = data['age']
        self.has_kids = data['has_kids']
        self.children = data['children']
    def __repr__(self):
        return f"""User:(
			first_name : {self.first_name}
			last_name : {self.last_name}
			email : {self.email}
			age : {self.age}
			has_kids : {self.has_kids}
			children : {self.children}
			)"""

user1 = User(people[0])
print(user1)
```
loop through it and call the `__init__()` constructor
```python
# 1 --
for user_dict in people:
    User(user_dict)
# 2 --
@classmethod
def create_users(cls):
# loop through people list and send each person dict to the constructor
	for each_dict in people:
		# print(each_dict)
		cls(each_dict)
```
---
## [Class and Static Methods - Platform](https://login.codingdojo.com/m/506/12458/87327)
`@classmethod` & `@saticmethod` decorators offer us the opportunity to organize our code in a better way
Functionality differences are minimal or non existent
### @classmethod
Function Decorators
- defined with a decorator `@classmethod`
- Instead of implicitly passing `self` into the method, we pass `cls`. This is reference to the class.
Thus: class methods have no access to the instance attribute or any attribute that starts with self
__Example__
Create a method to print all user info OR take an argument to print just one user info
```python
@classmethod
def print_info(cls, user_to_find_id = False):
	print(f"There are {len(cls.total_users)} users in our DB.")
	for user in cls.total_users:
		if user_to_find_id:
			# --------------
			if user.id == user_to_find_id:
			# --------------
				user.display_info()
		else:
			user.display_info()
```
### @staticmethod
[Class and Static Methods - Platform](https://login.codingdojo.com/m/506/12458/87327)
- defined within the class with a decorator `@staticmethod`
- no access to instance or class attributes
Thus:  if we need any existing values, they need to be passed in as arguments
__Example__
Create a `@staticmethod` to modularize some logic
```python
@staticmethod
def found_user(user, user_to_find_id):
	if user.id == user_to_find_id:
		return True
	else:
		return False
```
And refactor `@classmethod` `print_info()` to implement it:
```python
@classmethod
def print_info(cls, user_to_find_id = False):
	print(f"There are {len(cls.total_users)} users in our DB.")
	for user in cls.total_users:
		if user_to_find_id:
			# ----------------
			# Below implenting @staticmethod found_user()
			if User.found_user(user,user_to_find_id):
			# ------------
				user.display_info()
		else:
			user.display_info()
```

---
## Association Between Classes
[Association Between Classes - Platform](https://login.codingdojo.com/m/506/12458/87329)
Create a stand alone class to represent a post object
__post.py__
```python
class Post:
    def __init__(self, content):
        self.content = content
```
Associate that class to a user without defining it as an attribute.
__user.py__
```python
from post import Post
@classmethod
def create_post(cls, poster_id, post_content):
	# loop though users
	for poster in cls.all_users:
		# find the user by id who is posting
		if cls.found_user(poster, poster_id):
			# add that post to list of posts attribute
			poster.posts.append(Post(post_content))
```
`User.create_post(5, 'HIIIIIIIIIIIIIIII')`