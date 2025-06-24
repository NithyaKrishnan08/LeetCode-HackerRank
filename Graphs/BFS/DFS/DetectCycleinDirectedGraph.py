# Detect Cycle in a Directed Graph using DFS

'''
Given the number of vertices V and a list of directed edges, determine whether the graph contains a cycle or not.

Examples:

Input:  V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]

1
Cycle: 0 → 2 → 0 
Output:  true
Explanation:  The diagram clearly shows a cycle 0 → 2 → 0 

Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]

directed-1
No Cycle
Output:  false
Explanation:  The diagram clearly shows no cycle. 
'''

from typing import List

# TC: O(V + E)
# SC: O(V)

class Solution:
  def hasCycle(self, graph: List[List[int]]) -> bool:
    n = len(graph)
    visited = [False] * n
    recStack = [False] * n

    def dfs(node):
      visited[node] = True
      recStack[node] = True

      for neighbor in graph[node]:
        if not visited[neighbor]:
          if dfs(neighbor):
            return True
        elif recStack[neighbor]:
          return True
        
      recStack[node] = False
      return False
    
    for i in range(n):
      if not visited[i]:
        if dfs(i):
          return True
        
    return False
  
if __name__ == "__main__":
  graph = [[1], [2], [3], [1]]
  sol = Solution()
  print(sol.hasCycle(graph))
