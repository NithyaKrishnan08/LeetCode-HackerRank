# Graph Representation - Directed Graph

# Graph: 0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3, 3 -> 3
# Adjacency Matrix
# TC: O(N)
# SC: O(N * N)

n = 4
graph = [[0] * n for _ in range(n)]

# Add edges
graph[0][1] = 1
graph[0][2] = 1
graph[1][2] = 1
graph[2][0] = 1
graph[2][3] = 1
graph[3][3] = 1

# Check if edge exists between 2 -> 3
print(graph[2][3])  # Output: 1