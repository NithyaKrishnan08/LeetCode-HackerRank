# Articulation Point
# Articulation Point -> Nodes on whose removal the graph breaks into multiple components

# Time[] -> DFS time insertion
# low[] -> minimum lowest time insertion of all adjacent nodes apart from parent and visited nodes

'''
Problem Statement: Given an undirected connected graph with V vertices and adjacency list adj. You are required to find all the vertices removing which (and edges through it) disconnect the graph into 2 or more components.

Note: Indexing is zero-based i.e nodes numbering from (0 to V-1). There might be loops present in the graph.

Pre-requisite: Bridges in Graph problem & DFS algorithm.

Example 1:

Input Format:


Result: {0, 2}
Explanation: If we remove node 0 or node 2, the graph will be divided into 2 or more components.

Example 2:

Input Format:


Result: {1, 4}
Explanation: If we remove either node 1 or node 4, the graph breaks into multiple components.

'''
from typing import List

from typing import List

class Solution:
  def articulationPoints(self, n: int, connections: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(n)]
    for u, v in connections:
      graph[u].append(v)
      graph[v].append(u)

    tin = [-1] * n
    low = [-1] * n
    visited = [False] * n
    isArticulation = [False] * n
    timer = [0]

    def dfs(u: int, parent: int):
      visited[u] = True
      tin[u] = low[u] = timer[0]
      timer[0] += 1
      children = 0

      for v in graph[u]:
          if v == parent:
              continue
          if not visited[v]:
              dfs(v, u)
              low[u] = min(low[u], low[v])
              if low[v] >= tin[u] and parent != -1:
                  isArticulation[u] = True
              children += 1
          else:
              low[u] = min(low[u], tin[v])

      if parent == -1 and children > 1:
          isArticulation[u] = True

    for i in range(n):
      if not visited[i]:
        dfs(i, -1)

    result = [i for i, val in enumerate(isArticulation) if val]
    return result
