"""
Access SPecifiers in Python:
1. Public (default, available everywhere)
2. Protected (_variable_name, can be accessed within the class and its subclasses)
3. Private (__variable_name, can be accessed only within the class)

protected can be outside the class but it is not recommended
private cannot be accessed outside the class, python uses name mangling to make it private

Getter and Setter Methods:
1. Getter: Method that gets the value of a variable
2. Setter: Method that sets the value of a variable 
"""

class User:
    def __init__(self, name, email):
        self._name = name # protected variable
        self.__email = email # private variable

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

user1 = User("John", "john@example.com")
print(user1.get_email())
user1.set_email("john@yahoo.com")
print(user1.get_email())
