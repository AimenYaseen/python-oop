"""
Static attributes (also called class attributes) are attributes that are shared among all instances of a class.
Static attributes are defined outside of the class methods.
Static attributes are accessed using the class name.

To define a static method, use the @staticmethod decorator.
Static methods do not have access to the class or instance
"""

class User:
    active_users = 0 # static attribute

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.active_users += 1

    @staticmethod
    def display_active_users():
        return f"There are currently {User.active_users} active users"
    

user1 = User("John", "john@gmail.com")
user2 = User("Jane", "jane@yahoo.com")

print(User.display_active_users())


