#1.Delete the elements in an linked list whose sum is equal to zero

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_zero_sum_nodes(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head

    prefix_sum = 0
    seen = {0: dummy}

    curr = head
    while curr:
        prefix_sum += curr.val
        seen[prefix_sum] = curr
        curr = curr.next

    prefix_sum = 0
    curr = dummy
    while curr:
        prefix_sum += curr.val
        curr.next = seen[prefix_sum].next
        curr = curr.next

    return dummy.next
#2.Reverse a linked list in groups of given size

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_group(head, k):
    current = head
    prev = None
    next = None
    count = 0

    while current is not None and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    if next is not None:
        head.next = reverse_group(next, k)

    return prev
#3.Merge a linked list into another linked list at alternate positions

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_alternate(head1, head2):
    p1 = head1
    p2 = head2

    while p1 is not None and p2 is not None:
        temp = p1.next
        p1.next = p2
        p2 = p2.next
        p1.next.next = temp
        p1 = temp

    if p2 is not None:
        p1.next = p2

    return head1
#4.In an array, Count Pairs with given sum

def count_pairs(arr, target_sum):
    pairs = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs += 1
    return pairs
#5.Find duplicates in an array

def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            duplicates.append(abs(arr[i]))
    return duplicates
#6.Find the Kth largest and Kth smallest number in an array

def kth_smallest_largest(arr, k):
    sorted_arr = sorted(arr)
    kth_smallest = sorted_arr[k-1]
    kth_largest = sorted_arr[-k]
    return kth_smallest, kth_largest
#7.Move all the negative elements to one side of the array

def move_negative_to_left(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr
#8.Reverse a string using a stack data structure

def reverse_string(s):
    stack = []
    for c in s:
        stack.append(c)
    reversed_s = ""
    while len(stack) > 0:
        reversed_s += stack.pop()
    return reversed_s

# Example:
s = "Hello, World!"
reversed_s = reverse_string(s)
print(reversed_s)

#Output: "!dlroW ,olleH"
!dlroW ,olleH
#9.Evaluate a postfix expression using stack

def evaluate_postfix(expr):
    stack = []
    for char in expr:
        if char.isdigit():
            stack.append(int(char))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if char == "+":
                stack.append(val2 + val1)
            elif char == "-":
                stack.append(val2 - val1)
            elif char == "*":
                stack.append(val2 * val1)
            elif char == "/":
                stack.append(int(val2 / val1))
    return stack.pop()

# Example:
expr = "23+4*"
result = evaluate_postfix(expr)
print(result)

# Output: 14
20
#10.Implement a queue using the stack data structure

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def is_empty(self):
        return self.size() == 0

# Example:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue()) 
print(q.dequeue()) 
q.enqueue(4)
print(q.dequeue()) 
print(q.dequeue()) 
print(q.is_empty())
1
2
3
4
True
 