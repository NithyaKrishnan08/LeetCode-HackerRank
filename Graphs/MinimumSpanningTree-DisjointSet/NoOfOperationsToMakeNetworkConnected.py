# Number of operations to make network connected
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/

'''
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 

Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
'''

from typing import List

class DisjointSet:
  def __init__(self, n):
    self.rank = [0] * (n + 1)
    self.size = [0] * (n + 1)
    self.parent = [i for i in range(n + 1)]

  def findParent(self, node):
    if node == self.parent[node]:
      return node
    
    # Path Compression
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
  def makeConnected(self, n: int, connections: List[List[int]]) -> int:
    ds = DisjointSet(n)

    extra_edges = 0
    for u, v in connections:
      if ds.findParent(u) == ds.findParent(v):
        extra_edges += 1
      else:
        ds.unionBySize(u, v)

    conn_components = 0
    for i in range(n):
      if ds.findParent(i) == i:
        conn_components += 1

    answer = conn_components - 1
    if extra_edges >= answer:
      return answer
    else:
      return -1
    
if __name__ == "__main__":
  n = 6
  connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
  sol = Solution()
  result = sol.makeConnected(n, connections)
  print(result)
