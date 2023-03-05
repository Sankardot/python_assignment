numbers = (1,2,3,4,5,6,7,8,9)
even_count = 0
odd_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers:",even_count)
print("Number of odd numbers:",odd_count)