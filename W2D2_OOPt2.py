
# _ OOP Pt2
# < Starting off with lecture code from yesterday
# done todo Refactor User class to recieve a dictionary as an argument
# . @classmethod & @saticmethod
# . decorators offer us the opportunity to organize our code in a better way
# . Functionality differences are minimal
# < @classmethod
# ~   Instead of implicitly passing `self` into the method, we pass `cls`. 
# ~      This is reference to the class & constructor.
# ~   Thus: class methods have no access to the instance (or any attribute that starts with self)
# < @staticmethod
# ~   no access to instance or class attributes
# ~   Thus:  if we need any pre-existing values, they need to be passed in as arguments
#_ File imports -------------- 
# from dir import file
# from dir.file import variable/class
from pretendDBresponse import people
from post import Post
import sys

class User:
	#_ Class Attributes/Properties/DATA -------------- 
  all_users = []
  def __init__(self, data): # Constructor Method
    #_ Instance Properties/Attributes/DATA -------------- 
    # done attributes to refrence dictionary key value pairs not parameters -> positional arguments
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.age = data['age']
    self.has_kids = data['has_kids']
    self.children = data['children']
    self.posts = []
    User.all_users.append(self)
  
	#_ Methods/functions/ACTIONS -------------- 
	#! NOTICE indentation
  # def show_user_info():
    # print(f"First Name: {self.first_name}")
  def __repr__(self):
    return f"""
    User:
    ID : {self.id}
    First Name: {self.first_name}
    Last Name: {self.last_name}
    Email: {self.email}
    Age: {self.age}
    Has Kids: {self.has_kids}
    Children: {self.children}
    Posts: {self.posts}
    """

  def birthday(self):
    self.age += 1
    return self

  def name_children(self, new_name):
    self.children.append(new_name)
    return self
	
	# done Add a method to loop through pretend DB and create user objects
	# ~   import pretend DB	
  @classmethod
  def create_user(cls, db_users):
    for user in db_users:
      temp = cls(user)
      # print(type(temp))
      # print(temp)
      # print(cls.all_users)
    return "All Done"

	# done display_all_users() or just one by ID
	# ~   display all 
	# ~   display one (by id)
	# ~   utilize static helper method
  @classmethod
  def display_all_users(cls, user_to_find_id = False):
    # print(user_to_find_id)
    print(f"There are {len(cls.all_users)} users in our DB.")
    for user in cls.all_users:
      if user_to_find_id:
        if cls.found_user(user, user_to_find_id):
          print("Found The User")
          print(user)
      else:
        print(user)


  # ~ Associated Post class
  # ~ Values stored in self.posts attribue of the User class
  # ~ in this way each User instance has a list of thier own Post instance objects
  @classmethod
  def create_post(cls, poster_id, post_string):
    for poster in cls.all_users:
      if cls.found_user(poster, poster_id):
        poster.posts.append(Post(post_string))

  # ~ @staticmethod used on a method that does not need access to cls or self
  # ~ this is a "helper" method 
  @staticmethod
  def found_user(user, id_to_find):
    if user.id == id_to_find:
      return True
    else:
      return False

# _ -------------- TESTING --------------   #
user1 = {
	'id': 1,
	'first_name': 'Cameron',
	'last_name': 'Smith',
	'email': 'cs@email.com',
	'age': 35,
	'has_kids': True,
	'children': ['Harper', 'Walter']
}
newest_user = User(user1)
# print(people)
print(User.create_user(people))
# print(User.all_users)
User.create_post(5, "Houston we have liftoff")
User.display_all_users(5)

# , classes are smaller in bytes than dictionaries
# print(sys.getsizeof(user1))
# print(sys.getsizeof(newest_user))


# user1 = User("Cameron", "Smith", 35, True) 
# user2 = User("Timmy", "Jimmy-Jam", 34, False) 
# print(user1.first_name, user2.first_name)
# user2.has_kids = True
# user2.children.append("Biscut")
# user1.children = ["Harper", "Walter"]
# ^ print(user1, user2)
# ^ Without __repr__ this would print <__main__.User object at 0x000002EEAE0A3AF0>
# # user1.show_user_info()
# user2.birthday().name_children("Hercules")