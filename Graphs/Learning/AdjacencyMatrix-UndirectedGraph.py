# Graph Representation - Undirected Graph

# Adjacency Matrix
# TC: O(N)
# SC: O(N * N)
n = 4
graph = [[0] * n for _ in range(n)]

def add_edge(u, v):
  graph[u][v] = 1
  graph[v][u] = 1

add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 2)
add_edge(2, 3)

for row in graph:
  print(row)