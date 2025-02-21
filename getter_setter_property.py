"""

"""

class User:
    def __init__(self, name, email):
        self._name = name # protected variable
        self._email = email # protected variable

    # getter property
    @property
    def email(self):
        print("Getting Email")
        return self._email

    # setter property
    @email.setter
    def email(self, email):
        if '@' not in email:
            raise ValueError("Invalid email address")
        self._email = email

user1 = User("John", "jhon1@gmail.com")
print(user1.email)
user1.email = "change"
print(user1.email)