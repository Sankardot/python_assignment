#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [2, 4, 6, 8, 10]
target_sum = 12
pairs = find_pairs(arr, target_sum)
print(pairs)


# In[5]:


#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
arr = [1, 2, 3, 4, 5]
reverse_array_in_place(arr)
print(arr)


# In[6]:


#Q3. Write a program to check if two strings are a rotation of each other?

def is_rotation(s1, s2):
    """
    This function takes two strings as input and returns True if they are rotations of each other,
    otherwise it returns False.
    """
    # Check if the length of the two strings is the same
    if len(s1) != len(s2):
        return False

    # Concatenate the first string with itself to create a new string
    temp = s1 + s1

    # Check if the second string is a substring of the new string
    if s2 in temp:
        return True
    else:
        return False


# Testing the function
s1 = "hello"
s2 = "llohe"
print(is_rotation(s1, s2))  #Output: True

s3 = "python"
s4 = "onythp"
print(is_rotation(s3, s4))   #Output: False


# In[8]:


#Q4. Write a program to print the first non-repeated character from a string?

def first_non_repeated_character(string):
    # Create a dictionary to store the count of each character
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Loop through the string again to find the first non-repeated character
    for char in string:
        if char_count[char] == 1:
            return char

    # If no non-repeated character is found, return None
    return None

# Example:
string = "hello world"
result = first_non_repeated_character(string)
print(result)  # Output: 'h'


# In[9]:


#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

# In[1]:


def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         

n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods


# In[10]:


#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def postfix_to_prefix(postfix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    for char in postfix:
        if char not in operators:
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)
            
    return stack.pop()

# Example:
postfix = '34+5*'
prefix = postfix_to_prefix(postfix)
print(prefix) #Output: *+345


# In[11]:


#Q7. Write a program to convert prefix expression to infix expression.

def prefix_to_infix(prefix_expr):
    stack = []
    for i in range(len(prefix_expr)-1, -1, -1):
        if prefix_expr[i].isalnum():
            stack.append(prefix_expr[i])
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expr = f"({operand1}{prefix_expr[i]}{operand2})"
            stack.append(infix_expr)
    return stack.pop()



# In[12]:


#Q8. Write a program to check if all the brackets are closed in a given code snippet.

def check_brackets(code):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for char in code:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack:
                return False
            top = stack.pop()
            if brackets[top] != char:
                return False
    return not stack

#Example:
code_snippet = "{[()()]}"
if check_brackets(code_snippet):
    print("All brackets are closed.")
else:
    print("Some brackets are not closed.")


# In[17]:


#Q9. Write a program to reverse a stack.

def insert(s, last):
    if len(s) == 0:
        s.append(last)
        return
    top = s.pop()
    insert(s, last)
    s.append(top)
    return


def reverse(s):
    if len(s) <= 1:
        return
    temp = s.pop()
    reverse(s)
    insert(s, temp)
    return


if __name__=="__main__":
    s = [1, 2, 3]
    print(s)
    reverse(s)
    print("reversed :", s)


# In[18]:


#Q10. Write a program to find the smallest number using a stack.

def find_smallest(stack):
    if not stack:
        return None
    smallest = stack.pop()
    while stack:
        num = stack.pop()
        if num < smallest:
            smallest = num
    return smallest

#Example:
stack = [3, 7, 1, 9, 4, 2]
smallest = find_smallest(stack)
if smallest is not None:
    print("The smallest number in the stack is:", smallest)
else:
    print("The stack is empty.")


# In[ ]:
