#Q1.Implement Binary Search

def binary_search(arr, x):
    
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

#Example:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 7

result = binary_search(arr, x)
if result != -1:
    print(f"Found {x} at index {result}.")
else:
    print(f"{x} is not in the array.")
Found 7 at index 6.
#Q2.Implement Merge Sort

def merge_sort(arr):
    
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort each half
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    return arr

#Example:
arr = [9, 5, 7, 3, 1, 8, 6, 2, 4]
sorted_arr = merge_sort(arr)
print(sorted_arr)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Q3.Implement Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left_half = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right_half = [x for x in arr if x > pivot]
    
    return quick_sort(left_half) + middle + quick_sort(right_half)

#Example:

arr = [9, 5, 7, 3, 1, 8, 6, 2, 4]
sorted_arr = quick_sort(arr)
print(sorted_arr)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Q4.Implement Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#Example:
arr = [9, 5, 7, 3, 1, 8, 6, 2, 4]
sorted_arr = insertion_sort(arr)
print(sorted_arr)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Q5.Write a program to sort list of strings (similar to that of dictionary)

my_list = ['apple', 'Banana', 'orange', 'pear']
sorted_list = sorted(my_list, key=lambda x: x.lower())
print(sorted_list)
['apple', 'Banana', 'orange', 'pear']