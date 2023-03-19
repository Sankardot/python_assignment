def sum_list():
    num1_list = []
    n = int(input("Enter the number of elements :"))
    for i in range(n):
        num = int(input("Enter a number: "))
        num1_list.append(num)
    sum_of_list = sum(num1_list)
    return sum_of_list
print(sum_list())