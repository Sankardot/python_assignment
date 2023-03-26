#Write a Python program to square the elements of a list using map() function.
#Sample List: [4, 5, 2, 9]
#Square the elements of the list:
#[16, 25, 4, 81]
list_1 = [4,5,2,9]
ne_list1 = map(lambda x:x**2, list_1)
print(list(ne_list1))