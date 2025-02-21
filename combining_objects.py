class Owner:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Dog:
    def __init__(self, name, bread, owner):
        self.name = name
        self.bread = bread
        self.owner = owner

    def bark(self):
        print(f"{self.name} Woof!")


dog1 = Dog("Buddy", "Golden Retriever", Owner("John", "123 Main St"))
dog1.bark()
print(dog1.owner.name)
print(dog1.owner.address)

dog2 = Dog("Max", "Poodle", Owner("Jane", "456 Elm St"))
dog2.bark()
print(dog2.owner.name)
print(dog2.owner.address)
