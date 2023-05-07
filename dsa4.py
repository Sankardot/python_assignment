#Q1.Breadth First Traversal for a Graph

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start_node):
        visited = set()
        queue = deque()

        visited.add(start_node)
        queue.append(start_node)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            if node in self.graph:
                neighbors = self.graph[node]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

# Example:
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

print("Breadth First Traversal:")
graph.bfs(1)
Breadth First Traversal:
1 2 3 4 5 6 7 
#Q2.Depth First Traversal for a Graph

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_node)
        print(start_node, end=" ")

        if start_node in self.graph:
            neighbors = self.graph[start_node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

# Example:
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

print("Depth First Traversal:")
graph.dfs(1)
Depth First Traversal:
1 2 4 5 3 6 7 
#Q3.Count the number of nodes at given level in a tree using BFS

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def count_nodes_at_level(root, level):
    if not root:
        return 0

    queue = deque()
    queue.append((root, 0))
    count = 0

    while queue:
        node, current_level = queue.popleft()

        if current_level == level:
            count += 1

        if current_level > level:
            break

        for child in node.children:
            queue.append((child, current_level + 1))

    return count

# Example:
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

root.children = [node2, node3]
node2.children = [node4, node5, node6]
node3.children = [node7]
node5.children = [node8, node9]

level = 2
count = count_nodes_at_level(root, level)
print(f"Number of nodes at level {level}: {count}")
Number of nodes at level 2: 4
#Q4.Count number of trees in a forest

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = [[] for _ in range(num_nodes)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited):
        visited[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def count_trees(self):
        visited = [False] * self.num_nodes
        count = 0

        for node in range(self.num_nodes):
            if not visited[node]:
                self.dfs(node, visited)
                count += 1

        return count

# Example:
graph = Graph(5)  

graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(3, 4)

num_trees = graph.count_trees()
print("Number of trees in the forest:", num_trees)
Number of trees in the forest: 2
#Q5.Detect Cycle in a Directed Graph

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def has_cycle(self):
        visited = [False] * self.num_vertices
        path = [False] * self.num_vertices

        for node in range(self.num_vertices):
            if not visited[node] and self.dfs(node, visited, path):
                return True

        return False

    def dfs(self, node, visited, path):
        visited[node] = True
        path[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor, visited, path):
                    return True
            elif path[neighbor]:
                return True

        path[node] = False
        return False

# Example:
graph = Graph(4)  # Assuming there are 4 vertices in the directed graph

graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)

has_cycle = graph.has_cycle()
if has_cycle:
    print("Cycle is present in the directed graph")
else:
    print("Cycle is not present in the directed graph")
Cycle is present in the directed graph
# Miscellaneous Question
#Q1.**Implement n-Queen’s Problem

def is_safe(board, row, col, N):
    # Check if the current position is safe for a queen

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens_util(board, col, N):
    # Recursive utility function to solve the N-Queens problem

    # Base case: all queens are placed
    if col >= N:
        return True

    # Try placing the queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen at board[i][col]
            board[i][col] = 1

            # Recur to place the remaining queens
            if solve_n_queens_util(board, col + 1, N):
                return True

            # If placing the queen at board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    return False


def solve_n_queens(N):
    # Solve the N-Queens problem for a given N

    # Create an empty N×N chessboard
    board = [[0] * N for _ in range(N)]

    if not solve_n_queens_util(board, 0, N):
        print("No solution exists.")
    else:
        # Print the solution
        for row in board:
            print(" ".join(map(str, row)))


# Test the program with a 4x4 chessboard
solve_n_queens(4)
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0
 