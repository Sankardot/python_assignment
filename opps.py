# 1.Square Numbers and Return Their Sum

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2
    
p = Point(1, 3, 5)
result = p.sqSum()
print(result) 

# output
#35


# 2 Implement a Calculator Class

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num2 - self.num1
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num2 / self.num1
    
obj = Calculator(10, 94)
print(obj.add())       
print(obj.subtract())  
print(obj.multiply())  
print(obj.divide())  

# output

#104
#84
#940
#9.4


# 3. Implement the Complete Student Class

class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber


student = Student()
student.setName("John Doe")
student.setRollNumber(12345)
name = student.getName()
rollNumber = student.getRollNumber()
print("Name:", name)
print("Roll Number:", rollNumber)

# output
#Name: John Doe
#Roll Number: 12345

# 4: Implement a Banking Account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

account1 = SavingsAccount("Ashish", 5000, 5)
print(account1.title)  
print(account1.balance)  
print(account1.interestRate)  

# output  # Ashish is the title and 5000 is the balance and 5 is the interestRate.
#Ashish
#5000
#5

# 5: Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    def withdrawal(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def getBalance(self):
        return self.balance
    
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def interestAmount(self):
        return (self.balance * self.interestRate)/100

demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.deposit(500)
print(demo1.getBalance()) 

demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.withdrawal(500)
print(demo1.getBalance()) 

demo1 = SavingsAccount("Ashish", 2000, 5)
print(demo1.interestAmount()) 

# output 

#2500
#1500
#100.0
