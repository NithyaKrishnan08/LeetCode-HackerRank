# Number of Provinces

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
'''
from typing import List

class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = set()
    provinces = 0

    def dfs(city):
      for neighbor in range(n):
        if isConnected[city][neighbor] == 1 and neighbor not in visited:
          visited.add(neighbor)
          dfs(neighbor)

    for city in range(n):
      if city not in visited:
        visited.add(city)
        dfs(city)
        provinces += 1

    return provinces
  
if __name__ == "__main__":
  solution = Solution()
  isConnected = [[1,1,0],[1,1,0],[0,0,1]]
  result = solution.findCircleNum(isConnected)
  print(result)