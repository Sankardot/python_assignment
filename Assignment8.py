def count_upper_lower():
    user_str1 = input("Enter a string: ")
    upper_count = 0
    lower_count = 0
    for char in user_str1:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("No. of Upper case characters : ", upper_count)
    print("No. of Lower case characters : ", lower_count )
count_upper_lower()