#Q1.Implement Binary tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val):
        self.root = Node(root_val)
    
    def insert_left(self, parent, child_val):
        child = Node(child_val)
        parent.left = child
    
    def insert_right(self, parent, child_val):
        child = Node(child_val)
        parent.right = child
    
    def pre_order_traversal(self, node):
        if node is not None:
            print(node.val)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
    
    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.val)
            self.in_order_traversal(node.right)
    
    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.val)
            
#Example:
# create the binary tree
tree = BinaryTree(1)
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)
tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

# traverse the binary tree
print("Pre-order traversal:")
tree.pre_order_traversal(tree.root)

print("In-order traversal:")
tree.in_order_traversal(tree.root)

print("Post-order traversal:")
tree.post_order_traversal(tree.root)
Pre-order traversal:
1
2
4
5
3
In-order traversal:
4
2
5
1
3
Post-order traversal:
4
5
2
3
1
#Q2.Find height of a given tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val):
        self.root = Node(root_val)
    
    def insert_left(self, parent, child_val):
        child = Node(child_val)
        parent.left = child
    
    def insert_right(self, parent, child_val):
        child = Node(child_val)
        parent.right = child
    
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1

#Example:
# create the binary tree
tree = BinaryTree(1)
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)
tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

height = tree.height(tree.root)
print("Height of the tree is:", height)
Height of the tree is: 3
#Q3.Perform Pre-order, Post-order, In-order traversal

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val):
        self.root = Node(root_val)
    
    def insert_left(self, parent, child_val):
        child = Node(child_val)
        parent.left = child
    
    def insert_right(self, parent, child_val):
        child = Node(child_val)
        parent.right = child
    
    def pre_order_traversal(self, node):
        if node is not None:
            print(node.val)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
    
    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.val)
            self.in_order_traversal(node.right)
    
    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.val)
#Example:
# create the binary tree
tree = BinaryTree(1)
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)
tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

# perform pre-order traversal
print("Pre-order traversal:")
tree.pre_order_traversal(tree.root)

# perform in-order traversal
print("In-order traversal:")
tree.in_order_traversal(tree.root)

# perform post-order traversal
print("Post-order traversal:")
tree.post_order_traversal(tree.root)
Pre-order traversal:
1
2
4
5
3
In-order traversal:
4
2
5
1
3
Post-order traversal:
4
5
2
3
1
#Q4.Function to print all the leaves in a given binary tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_leaves(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        print(node.val)
    print_leaves(node.left)
    print_leaves(node.right)
#Q5.Implement BFS (Breath First Search) and DFS (Depth First Search)

from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in vertices}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()

    def dfs(self, start):
        visited = set()
        self._dfs_helper(start, visited)

    def _dfs_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

#Example:
# create a graph
vertices = [0, 1, 2, 3, 4, 5, 6]
graph = Graph(vertices)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 6)

# perform BFS starting from vertex 0
print("BFS:")
graph.bfs(0)

# perform DFS starting from vertex 0
print("DFS:")
graph.dfs(0)
BFS:
0 1 2 4 3 5 6 
DFS:
0 1 2 3 4 5 6 
#Q6.Find sum of all left leaves in a given Binary Tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    if not root:
        return 0

    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sum_of_left_leaves(root.right)

    return sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)

#Example:
# create a binary tree
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(sum_of_left_leaves(root))  
24
#Q7.Find sum of all nodes of the given perfect binary tree

def sum_of_nodes_in_perfect_binary_tree(height):
    return (2**(height+1) - 1) * (1 + (2**height)) // 2

#Example:
sum = sum_of_nodes_in_perfect_binary_tree(3)
print(sum)
67
#Q8.Count subtress that sum up to a given value x in a binary tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_subtrees_with_given_sum(root, x):
    count = 0

    def traverse(node):
        nonlocal count
        if not node:
            return 0

        left_sum = traverse(node.left)
        right_sum = traverse(node.right)

        curr_sum = node.val + left_sum + right_sum

        if curr_sum == x:
            count += 1

        return curr_sum

    traverse(root)
    return count
#Q9.Find maximum level sum in Binary Tree

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_level_sum(root):
    if not root:
        return 0

    queue = deque([root])
    max_sum = float('-inf')
    level = 0

    while queue:
        level += 1
        level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

    return max_level

#Example:
# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

max_level = max_level_sum(root)
print(max_level) 
3
#Q10.Print the nodes at odd levels of a tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_odd_levels(root):
    if not root:
        return

    print_odd_levels_helper(root, 1)

def print_odd_levels_helper(node, level):
    if not node:
        return

    if level % 2 == 1:
        print(node.val)

    print_odd_levels_helper(node.left, level + 1)
    print_odd_levels_helper(node.right, level + 1)
    
#Example:
# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print_odd_levels(root)  
1
4
5
6
7