# Most stones removed with same row or column
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

'''
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.
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
  def removeStones(self, stones: List[List[int]]) -> int:
    maxcoord = 10000
    ds = DisjointSet(2 * maxcoord + 1)

    used_nodes = set()
    for x, y in stones:
      row = x
      col = y + maxcoord + 1
      ds.unionBySize(row, col)
      used_nodes.add(row)
      used_nodes.add(col)

    unique_parents = set()
    for node in used_nodes:
      unique_parents.add(ds.findParent(node))

    return len(stones) - len(unique_parents)
  
if __name__ == "__main__":
  sol = Solution()
  stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
  result = sol.removeStones(stones)
  print(result)