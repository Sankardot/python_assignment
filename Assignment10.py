#Write a Python program to triple all numbers of a given list of integers. Use Python map.
#sample list: [1, 2, 3, 4, 5, 6, 7]
#Triple of list numbers:
#[3, 6, 9, 12, 15, 18, 21]
nums = (1, 2, 3, 4, 5, 6, 7) 

print("Original list: ", nums)

result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))
