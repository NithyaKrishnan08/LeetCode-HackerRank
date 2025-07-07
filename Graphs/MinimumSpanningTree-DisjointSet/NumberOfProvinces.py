# Number of Provinces
# https://leetcode.com/problems/number-of-provinces/description/

'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''

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
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    ds = DisjointSet(n)

    for i in range(n):
      for j in range(n):
        if isConnected[i][j] == 1:
          ds.unionBySize(i, j)

    province_cnt = 0
    for i in range(n):
      if ds.parent[i] == i:
        province_cnt += 1


    return province_cnt
  
if __name__ == "__main__":
  isConnected = [[1,0,0],[0,1,0],[0,0,1]]
  sol = Solution()
  result = sol.findCircleNum(isConnected)
  print(result)