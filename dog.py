Assignment 2
👉 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
🔴 d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

    def get_info(self):
        print("Coat Color: ", self.coat_color)


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, size):
        super().__init__(name, age, coat_color)
        self.size = size

    def unique_method1(self):
        print("This is a unique method of Jack Russell Terrier")
        
    def unique_method2(self):
        print("This is another unique method of Jack Russell Terrier")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def unique_method1(self):
        print("This is a unique method of Bulldog")
        
    def unique_method2(self):
        print("This is another unique method of Bulldog")


# Creating Dog object
dog1 = Dog("Buddy", 3, "Brown")
dog1.description()  # Output: Name: Buddy \n Age: 3
dog1.get_info()  # Output: Coat Color: Brown

# Creating JackRussellTerrier object
jack_russell1 = JackRussellTerrier("Max", 5, "White", "Small")
jack_russell1.description()  # Output: Name: Max \n Age: 5
jack_russell1.get_info()  # Output: Coat Color: White
jack_russell1.unique_method1()  # Output: This is a unique method of Jack Russell Terrier

# Creating Bulldog object
bulldog1 = Bulldog("Rocky", 4, "Fawn", "Heavy")
bulldog1.description()  # Output: Name: Rocky \n Age: 4
bulldog1.get_info()  # Output: Coat Color: Fawn
bulldog1.unique_method2()  # Output: This is another unique method of Bulldog