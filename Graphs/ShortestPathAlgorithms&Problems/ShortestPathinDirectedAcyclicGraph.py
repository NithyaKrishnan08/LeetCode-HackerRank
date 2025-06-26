# Shortest Path in Directed Acyclic Graph (DAG)

'''
Given a Directed Acyclic Graph of V vertices from 0 to n-1 and a 2D Integer array(or vector) edges[ ][ ] of length E, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i.

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex.

Examples :

Input: V = 4, E = 2, edges = [[0,1,2], [0,2,1]]
Output: [0, 2, 1, -1]
Explanation: Shortest path from 0 to 1 is 0->1 with edge weight 2. Shortest path from 0 to 2 is 0->2 with edge weight 1. There is no way we can reach 3, so it's -1 for 3.
Input: V = 6, E = 7, edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
Output: [0, 2, 3, 6, 1, 5]
Explanation: Shortest path from 0 to 1 is 0->1 with edge weight 2. Shortest path from 0 to 2 is 0->4->2 with edge weight 1+2=3. Shortest path from 0 to 3 is 0->4->5->3 with edge weight 1+4+1=6. Shortest path from 0 to 4 is 0->4 with edge weight 1.Shortest path from 0 to 5 is 0->4->5 with edge weight 1+4=5.
Constraint:
1 <= V <= 100
1 <= E <= min((N*(N-1))/2,4000)
0 <= edgesi,0, edgesi,1 < n
0 <= edgei,2 <=105
'''

# Step 1: Do a topological sort of the graph
# Step 2: Take the nodes out of the stack one by one and relax the edges

# Time Complexity: O(V + E)
# Space Complexity: O(V + E) for adjacency list, visited, stack, and distance arrays.

from typing import List
from collections import defaultdict

class Solution:
  def shortestPath(self, V: int, edges: List[List[int]], src: int) -> List[int]:
    # Build the adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v, weight in edges:
      graph[u].append((v, weight))

    # Step 1: Topological sort using DFS
    visited = [-1] * V
    stack = []

    def dfs(node):
      visited[node] = 1
      for neighbor, _ in graph[node]:
        if visited[neighbor] == -1:
          dfs(neighbor)
      stack.append(node)

    for i in range(V):
      if visited[i] == -1:
        dfs(i)
    
    # Step 2: Relax edges based on topological order
    distance = [float('inf')] * V
    distance[src] = 0

    while stack:
      node = stack.pop()
      if distance[node] != float('inf'):
        for neighbor, weight in graph[node]:
          if distance[neighbor] > distance[node] + weight:
            distance[neighbor] = distance[node] + weight

    # Replace inf with -1 for unreachable nodes
    for i in range(V):
      if distance[i] == float('inf'):
        distance[i] = -1

    return distance
  
if __name__ == "__main__":
  edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
  V = 6
  src = 0
  sol = Solution()
  result = sol.shortestPath(V, edges, src)
  print(result)
