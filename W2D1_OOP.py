
# _ OOP
# < A programming paradigm that:
  # . organizes data and behavior into reusable and self-contained objects(CLASSes). 
  # < These class objects contain both 
    # . self.data (attributes or properties) 
      # > AND 
    # . methods() (functions or procedures) 
  # < that operate on the data. 
# ! The primary purpose of OOP is to increase the reusability and maintainability of code

# > Class
  # ~ A class is a blueprint or a template for creating objects. 
  # ~ It defines the properties (attributes) and methods (functions) that the objects of the class will have.
  # ~ Represents what each INSTANCE(object) will look like

# > OBJECT
  # ~ An object is a real-world entity that is an instance of a class. 
  # ~ It represents a unique occurrence of a class.
  # ~ All users have the same structure but my info is different than yours

# todo SYNTAX:
# , starts with the keyword
# ! class 
# , followed by
# ! ClassName (capitalized and singular) 
# , and a 
# ! colon :

class User:
	#_ Class Attributes/Properties/DATA
  all_users = []
  def __init__(self, fname, lname, age, has_kids): # Constructor Method
    #_ Instance Properties/Attributes/DATA
    self.first_name = fname
    self.last_name = lname
    self.age = age
    self.has_kids = has_kids
    self.children = []
  
	#_ Methods/functions/ACTIONS
	#! NOTICE indentation
  # def show_user_info():
    # print(f"First Name: {self.first_name}")
  def __repr__(self):
    return f"""
    User:
    First Name: {self.first_name}
    Last Name: {self.last_name}
    Age: {self.age}
    Has Kids: {self.has_kids}
    Children: {self.children}
    """

  def birthday(self):
    self.age += 1
    return self

  def name_children(self, new_name):
    self.children.append(new_name)
    return self

user1 = User("Cameron", "Smith", 35, True) 
user2 = User("Timmy", "Jimmy-Jam", 34, False) 
print(user1.first_name, user2.first_name)
user2.has_kids = True
user2.children.append("Biscut")
user1.children = ["Harper", "Walter"]
print(user1, user2)
# user1.show_user_info()
user2.birthday().name_children("Hercules")
