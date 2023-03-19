#Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reverse_string():
    user_str1 = input("Enter a string: ")
    reversed_str1 = user_str1[::-1]
    return reversed_str1
print(reverse_string())

