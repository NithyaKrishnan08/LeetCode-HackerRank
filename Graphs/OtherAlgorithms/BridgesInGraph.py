# Bridges in Graph - Using Tarjan's Algorithm of time in and low time
# Bridge -> Any edge when removed in a graph, it is broken into 2 or more components

# Time[] -> DFS time insertion
# low[] -> minimum lowest time insertion of all adjacent nodes apart from parent

'''
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
'''
# Time: O(V + E) — one DFS traversal
# Space: O(V + E) — graph and recursion stack

from typing import List

class Solution:
  def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    # Step 1: Build the graph
    graph = [[] for _ in range(n)]
    for u, v in connections:
      graph[u].append(v)
      graph[v].append(u)

    # Step 2:Initialize arrays
    time = [-1] * n
    low = [-1] * n
    visited = [False] * n
    timer = [0] # use list for mutability in nested function
    bridges = []

    # Step 3: DFS function
    def dfs(u: int, parent: int):
      visited[u] = True
      time[u] = low[u] = timer[0]
      timer[0] += 1

      for v in graph[u]:
        if v == parent:
          continue
        if not visited[v]:
          dfs(v, u)
          low[u] = min(low[u], low[v])

          # Bridge condition
          if low[v] > time[u]:
            bridges.append([u, v])
        else:
          # Back edge
          low[u] = min(low[u], time[v])
    
    # Step 4: Call DFS for all components
    for i in range(n):
      if not visited[i]:
        dfs(i, -1)
    
    return bridges
  
if __name__ == "__main__":
  sol = Solution()
  n = 4
  connections = [[0,1],[1,2],[2,0],[1,3]]
  result = sol.criticalConnections(n, connections)
  print(result)

