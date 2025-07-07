# Kruskal's Algorithm
# This algorithm helps to find MST

# Sort all the edges according to the weight

'''
Problem Statement: Given a weighted, undirected, and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.

Example 1:

Input Format: 
V = 5, edges = { {0, 1, 2}, {0, 3, 6}, {1, 2, 3}, {1, 3, 8}, {1, 4, 5}, {4, 2, 7}}


Result: 16
Explanation: The minimum spanning tree for the given graph is drawn below:
MST = {(0, 1), (0, 3), (1, 2), (1, 4)}


Example 2:

Input Format: 
V = 5, 
edges = { {0, 1, 2}, {0, 2, 1}, {1, 2, 1}, {2, 3, 2}, {3, 4, 1}, {4, 2, 2}}


Result: 5
Explanation: The minimum spanning tree is drawn below:
MST = {(0, 2), (1, 2), (2, 3), (3, 4)}

'''
# TC: O(E log E + E α(V))
# SC: O(V + E)
from typing import List

class DisjointSet:
  def __init__(self, n):
    self.rank = [0] * (n + 1)
    self.size = [1] * (n + 1)
    self.parent = [i for i in range(n+1)]

  def findParent(self, node):
    if node == self.parent[node]:
      return node
    
    # Path compression
    self.parent[node] = self.findParent(self.parent[node])
    
    return self.parent[node]
  
  def unionByRank(self, u, v):
    ultParent_u = self.findParent(u)
    ultParent_v = self.findParent(v)

    if ultParent_u == ultParent_v:
      return
    
    if self.rank[ultParent_u] < self.rank[ultParent_v]:
      self.parent[ultParent_u] = ultParent_v
    elif self.rank[ultParent_v] < self.rank[ultParent_u]:
      self.parent[ultParent_v] = ultParent_u
    else:
      self.parent[ultParent_v] = ultParent_u
      self.rank[ultParent_u] += 1

  def unionBySize(self, u, v):
    ultParent_u = self.findParent(u)
    ultParent_v = self.findParent(v)

    if ultParent_u == ultParent_v:
      return
    
    if self.size[ultParent_u] < self.size[ultParent_v]:
      self.parent[ultParent_u] = ultParent_v
      self.size[ultParent_v] += self.size[ultParent_u]
    else:
      self.parent[ultParent_v] = ultParent_u
      self.size[ultParent_u] += self.size[ultParent_v]

class Solution:
  def spanningTree(self, V: int, adj: List[List[List[int]]]) -> int:
    edges = []
    for i in range(V):
      for neighbor in adj[i]:
        adjNode = neighbor[0]
        wt = neighbor[1]
        edges.append((wt, i, adjNode)) # (weight, u, v)

    # Remove duplicates in undirected graph by sortign and using a set
    edges = list(set((wt, min(u, v), max(u, v)) for wt, u, v in edges))
    edges.sort()

    ds = DisjointSet(V)
    mst_weight = 0

    for wt, u, v in edges:
      if ds.findParent(u) != ds.findParent(v):
        mst_weight += wt
        ds.unionBySize(u, v)
    
    return mst_weight
  
if __name__ == "__main__":
  V = 5
  input_edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
  
  adj = [[] for _ in range(V)]
  for u, v, w in input_edges:
      adj[u].append([v, w])
      adj[v].append([u, w])  # since it's undirected

  sol = Solution()
  mstWt = sol.spanningTree(V, adj)
  print("The sum of all the edge weights:", mstWt)
