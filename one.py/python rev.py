# python  is dynamic programming language it is used fro development purpose and  for machine learning purpose 

# invented by guido van rossum in 1991 

# programming is the process of creating of set of instructions that tell a computer to perform a task 

# coding is the step by step instructions that got computers to do what you want them to do 


# programiing = plan 
# coding = implementation 

# “Python is mainly called an interpreted language because execution happens through the Python interpreter. 
# But before execution, Python source code is compiled into bytecode.”


# # python is high level programming language 
# “Python is an interpreted language, but internally it also uses compilation.”

# complier converts the high level programming language to low level programming langugae such as machine code 

# it will excute the code at once 
# code execution is fast 
# supoose if we have error in 3rd line of the code it will execute all lines of the code 
# it is used for c, c++


# interpreter : it checks the code line by line 
# slow execution 
# supoose u have 3 rd line of code it will stop their only 
# pyhton , javascript, 



# extension = the pyhton file is saveed as .Py

# pvm- pyhton virtual machine 



# pyhton is interpreted language object oreinted and high level programiimng language 

# synax set of rules is called as a syntax 



# mutable they can be chnaged after creation

# dictonary, list, set 


 
# immutable  they cant be changed after creaation 
# int, float, string, tuple , bool, frozen set



# variables is which stores the value of addres is called as variable 
# it is defined with id 
# it finds the memory address
# we cant print  multiple variables with one value 




# identifiers : “Identifiers are user-defined names given to variables, functions, classes, and objects in Python.”

# #rules:
# Can contain letters, numbers, _
# Cannot start with number
# Cannot use keywords like class, for, if
# Case-sensitive- upper case and lower case 










# A function in Python is a block of code that performs a specific task and can be reused whenever needed.

# Instead of writing the same code again and again, you put it inside a function and call it whenever you want.

# function :block of codde is called as a function 

# module:collection of function is called a module 

# package:collection of modules is called package 

# library: collection of package is called as library

# frame work a collection of everything is called frame work 




# ide:integreted development environment is software for building application 
# that combines common developers tools into single graphical user interface 


# comments:they are ignored by the complier 
# they are two types they are 
# single line , mutilple line 
# #               """"



# variable is container which stores the value of addres 
# in pyhton you dont want to decalre the type of varible 
# a varible i screated at the moment we first assign the value to it 
# we stored in memory of value it is called a address 

 
# print("sankar")


# sankar = 20
# print(sankar)



# a=b=c =100
# print(b)

# multiple varobels can pass throw one value in variables 


# types of conversion in python

# the are process of converting the value of one  datatype to antother data type is called a type conversion 
# they are two types they are 

# implict and explict 


# implict type conversion : done automatically on pyhton 

# no data losss

# a = 1000#int 
# print(float(a))



# explict coversion:manaul uiing 
# the user manually converts one data type to antother data type 
# # data loss

# a = 1000.0
# print(int(a))



# Garbage Collection in Python, you can explain like this:

# “Garbage collection in Python is the process of automatically freeing memory by removing unused objects.”

# Simple explanation:

# When an object is no longer used in the program, Python automatically deletes it and releases memory.
# This helps in memory management.







# #inputfunction : the inputfunction is used to take the input from user during the exccution 
# a=input("enter the name: ")
# print(a)




# operators is genarelly used to perform operations on the values and variables  is called operators 




# control staments : control statements are used to change the flow of execution is calledd  control stamnts 
# it is divides into three types 
# conditonal staments , jumping staments , looping statments 

# conditonal staments  sre also called as decison making stamnts  
# if 
# if else 
# if elif 
# nested if else 



# condtional statemts are alsi called decison making statments 
# we use those statments while we  want to excutte a block of code while the given is condition is true 


# num1 = int(input("enter the  first number:" ))
# num2 = int(input("Enter the second number:"))
# if num1>num2:
#     print('greater than num1')
# elif num2 > num1:
#     print("greater than number2")
# else:
#     print("Both are equal number")



# loopin statments are alos now as iterative staments if we want to excute a group 
# of stament multiplt times then we should go for a looping kind of execution 
# for loop and while loop 


# while loop:
#     “A while loop is used to execute a block of code repeatedly as long as a condition is true.” 


# i = 1
# while i < 10:
#     print(i)
#     i+=1


# a = 12
# while a < 34:
#     print(a)
#     a+=1



# i = 6
# while i <=95:
#     if i ==13:
#         print("three")
#     else:
#         print(i)
#     i +=1






# for loop this type of loop executtes a code  block multiples times
# “A for loop is used to iterate over a sequence like a list, tuple, string, or range.”

# in foor loop each and every element will be looped and it will be eneded at data ends 



# for a in 'adaru':
#     print(a)


# for day in range (1,3):
#     print("day", day)
    
#     water =1 
#     while water <=2:
#         print("drink water")
#         water +=1
        
# range function : it is used genrare a sequence  of number 
# synrtax(start , stop , step)


# for i in range(0,11,2):
#     print(i)



# transfer statemnts:  are also know as jumping statments 
# # continue , pass, break 
# are used to change the  flow of program by jumping from one part of the code to another escpecially inside loop 
 
# exit loop earlu 
# skip the iteration do nothing is called a place holder 

# break , continue , pass 


# break : exits the loop immediately when you want stop a loop 

# for i in range(1,6):
#     if i == 3:
#         break
#     print(i)
   
   

# continue : skips to the Next iteration  when u want to skip onw ture 

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)
    
# pass:does nothing IT is place holder use it when code is needed syntatically but not yet written 


# range function : it is used to genrate the sequence of number

# it is used often used with loop especially for  loops 

# syntax(start, stop, step)



# indexing : Indexing is the process of accessing elements from a sequence like a string, list, or tuple using their position number.”

# they are divide into postive an negativ



# postive indexing: starts from 0  and it is called a forword indexing 


# data = ['a', 'b', 'c', 'd']
# print(data[0])
# print(data[2])



# #negative ondexing : it starts from -1 it is called negative indexing  back word indexing 
# data = ['a', 'b', 'c', 'd']
# print(data[-1])
# print(data[-2])



# concatenation: joining the sequence like string list tuole togetgher is  called concatenation using + operator 

# a = [1,2]
# b = [2,3]
# print(a+b)



# slicing is list methos 
# it is technique to extract a subpart  from the sequence like a list string , tuple 


# n = [10, 20, 30 ,40, 50]
# print(n[1:4])




# match cases inpyhton used fro multiple condtion checking 
# it is similar to switch case in one another programming language 

#  match ----> cheacks the value 
#  case ----->conditions
#  _  -----> deffault value 
 
 
 
# day = 0
# match day:
#     case 1:
#         print("mOnday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wed")
#     case _:
#         print("Invalid")


# list compareshion is method of creating short and simple way to creata a list using single line code 

# sqaure =[x*x for x in range(1,5)]
# print(sqaure)







# list is mutable it has methods of 12 methods tha
# they are 


# list  has 12 methods 

# append : add the element in list at the end 

# extend : adds the multiple item 

# insert add specific position 

# remove : removes specific values

# pop: removes using Index

# clear:
#     removes all the item 
    
# index: finds index value 

# count:count occurence

# sort : sort the list 

# reverse: reverse the lisst 

# copy :copy the list 






# tuple is collection of elements sepated by comma and enclosed the parenthesis it is immutable 
# count()
# index()

# mutable: it can be changed after creation 
# dictnary, list , set 

# immutable is can be changed after the creation 
# int, float, string, complex, boolean 




# Data Type	Approximate Number of Methods



# List	 12 


# Tuple	2



# Set	17



# Dictionary	11




# String	45+



# LIST ALLOWS DUPLICATES 

# TUPLE ALLOWS DUPLICATS 


# STRING ALLOWS DUPLICATES 


# SET NOT ALLOW DUPLICATES IT REMOVES THE DUPICATES 


# DICTONARY 

# KEYS DOESNOT ALLOW DUPLICATES

# VALUES CAN ALLOW DUPLICATES 







# In Python, collections like list, tuple, set, and dictionary support heterogeneous data, 
# while strings store homogeneous character data.”




# list, tuple, set, and dictionary are supoorted both 

# string only  homogeneous data 


# HOMOGENOUS : IT ALL THE ELEMENTS ARE SAME 

# HETROGENOUS : ALL THE ELEMENTS ARE HETRO GENOUS


# set: is unorder list it is mutable data type it is defined with curely bracles and it doesnot allow duplicates 

# it has 17 built in methods 


# s = {1,3,4}
# # s.add(9)
# # print(s)
# # ----add the element to the set ONLY ONE 



# s.update([4, 5])
# print(s)----------------------ADDS A MULTIPLE ELEMENT 


# s={1,2,4,19}
# s.remove(8)
# print(s) ----------------if suppose the key balue is not present in the set it will give key error 

# s={1,2,4,19}
# s.discard(10)  # no error if the value is also not present it not give error 




# s={1,2,4,19}
# s.pop()
# print(s)---------------------------remove the first eleemnt from the set 



# s={1,2,4,19}
# s.clear()
# # print(s)---------------------------------REMOVE ALL THE ELEMENTS FROM THE LIST 





# set operators

# Method	Meaning	Symbol

# union()	Combine all unique elements	`


# intersection()	Common elements	&


# difference()	Present in first only	-


# symmetric_difference()	Not common in both	^




# a = {1, 2, 3}
# b = {2, 3, 4}

# # union() -> Combines all unique elements
# print("Union:")
# print(a.union(b))
# print(a | b)

# # intersection() -> Common elements
# print("\nIntersection:")
# print(a.intersection(b))
# print(a & b)

# # difference() -> Elements in first set only
# print("\nDifference:")
# print(a.difference(b))
# print(a - b)

# # symmetric_difference() -> Not common in both
# print("\nSymmetric Difference:")
# print(a.symmetric_difference(b))
# print(a ^ b)



# a = {1, 2}
# b = {1, 2, 3, 4}
# c = {5, 6}

# # issubset() -> Checks whether all elements of a are in b
# print("Subset:")
# print(a.issubset(b))   # True

# # issuperset() -> Checks whether  one contains all elements of another elements 
# print("\nSuperset:")
# print(b.issuperset(a))   # True

# # isdisjoint() -> Checks whether sets have no common elements
# print("\nDisjoint:")
# print(a.isdisjoint(c))   # True











# list is mutable and it is defined with []
# it has 12 methods and 
# it is order collection 
# it allows duplicatews and we can perform indexing 





# list compareshesion : method of creating   list compreshion is a short and simple way to create a list using a single line of code 

# square =[X * X for X in range(1,5)]
# print(square)


# square =[]
# for x in range(1,5):
#     square.append(x*x)
# print(square)


# by using list compareshesion is short and simple way to create a list using a single line of code 



# tuple is collection os elements separted by comma and enclose with parenthesis 
# it is immutable and and it has 2 methods and 
# we can perforn indexing and it aloows duplicates 
# it is oorder collection 
# #it is faster than list 


# s = (1,23,3)
# print(type(s))
# print(s)



# set is mutbale and it defined {} curely bracles and it is unorder list 
# it doesnot accpet  duplicated values 
# we can not  perform indexing 

# but we can perform a concatention in the set with union operator 
# set has 17 built in methods in python 


# #s = {1,2,2,3}          -----> removes the dupicates from the set
# print(id(s))
# print(type(s))
# print(s)




# dictonary is  mutable and it is defined with {} curely bracles and 
# it is order list 
# w can perform a indexing by accesing the keys in dictonary 
# if we  want  to acces the value we need acces the key first 

# dict keys can be immutable 

# dict values can be mutable , immutable  



























# # 1. Without Argument and Without Return
# # Even-Odd Program
# def even_odd():
#     n = int(input("Enter a number: "))

#     if n % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")

# even_odd()

# function takes input inside itself and prints output directly without returning anything.








# Without Argument and With Return
# Even-Odd Program
# def even_odd():
#     n = int(input("Enter a number: "))

#     if n % 2 == 0:
#         return "Even Number"
#     else:
#         return "Odd Number"

# result = even_odd()

# print(result)

# Function takes input inside itself and returns the result to be printed outside.







# With Argument and Without Return
# # Even-Odd Program
# def even_odd(n):

#     if n % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")

# even_odd(10)
# even_odd(7)

# Function receives input while calling and prints output directly inside the function.





# With Argument and With Return
# # Even-Odd Program
# def even_odd(n):

#     if n % 2 == 0:
#         return "Even Number"
#     else:
#         return "Odd Number"

# result = even_odd(8)

# print(result)

# Function receives input while calling and returns the result to be used or printed outside the function.








# Character is Vowel or Not
# def check_vowel(ch):

#     if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
#         print("Vowel")
#     else:
#         print("Not a Vowel")

# check_vowel('a')
# check_vowel('b')





# # Alphabet or Not
# def check_alphabet(ch):

#     if ch.isalpha():
#         print("It is an Alphabet")
#     else:
#         print("It is Not an Alphabet")

# check_alphabet('A')
# check_alphabet('5')



# # Special Character or Not
# def special_character(ch):

#     if not ch.isalnum():
#         print("Special Character")
#     else:
#         print("Not a Special Character")

# special_character('@')
# special_character('A')
# special_character('5')







# print() is used to display the output on the screen, 
# Value is shown immediately
# Does not send value back to the caller


# return is used to send the value back from the function so it can be stored or reused later in the program.
# Useful for further calculations














# Recursive function : a function calls itself agian and agian until a conditon is met
# base condition is satisfied to solve a problem step by step.





# factorial: factorial is a number is multiplication of that number with
# all positive integer less than it up to 1. 






# Factorial Using Recursion
# def factorial(n):

#     if n == 1:                        ---->base condition
#         return 1

#     return n * factorial(n - 1)        -------->recursive call

# print(factorial(5))


# # factorial without recursion:
# def factorial(n):

#     result = 1

#     for i in range(1, n + 1):
#         result = result * i

#     return result

# print(factorial(5))



# Recursive

# Problem is solved by:       Function calling itself.



# Non-Recursive

# Problem is solved by:        Repeating loop execution.












# diff between the recursive non recursive function :
    
    
# The main difference is that recursive functions solve problems by calling themselves repeatedly,
# while non-recursive functions use loops for iteration without self-calling.

# Uses of Recursion
# Factorial
# Fibonacci series
# Tree traversal
# Graph algorithms
# Backtracking problems









# Arguments: arguments are values passed to a function while calling it 

# def add(a,b):
#     print(a+b)
# add(1,3)


# a and b → Parameters
# 10 and 20 → Arguments



# types of arguments :

# positional:  In Positional Argument during function call, Number of values passed must be same as no. 
# of arguments defined in function defination
    


# def student(name, age):
#     print(name, age)

# student("Ram", 22)






# # Keyword Arguments: Arguments passed using parameter names.
#  During function call values are passed along with argument name


# def student(name, age):
#     print(name, age)
# student(age=22, name="Ram")





# # Default Arguments: Function already has default value.

#  if an argument is assigned with a value then it is said to be default argument, 
#  if we pass value to this argument it will be overridden otherwise it will take default value

# def country(name="India"):
#     print(name)

# country()







# Arbitrary Arguments in Python (*args)

# Arbitrary arguments allow a function to accept multiple values as arguments.
# It uses *args.
# In Arbitary variable argument during function defination argument is prefixed with single *,
# #     This argument takes 0 to n nummber of values and packs it in the form of Tuple

# def numbers(*args):
#     print(args)

# numbers(10, 20, 30, 40)


# def fun(*arg):
#     print(arg, type(arg))
    
# fun(1,2,3,4,5)
# fun()
# fun('don','khan','iron man',100)


# def agg(*args):
#     print(sum(args))
#     print(min(args))
#     print(max(args))

# agg(1,2,3,4,5)
# agg(10,20,30,40)




# Arbitrary Keyword arguments : accepts multiples keyword arguments 
#     # During function defination argument will be prefixed with double *,
#     # This argument takes 0 to n number of values and packs it in the form of dictionary
    
# def fun(**args):
#     print(args,type(args))

# fun(a=10,b=20)



