# Shortest Distance in a Binary Maze

'''
Problem Statement: 

Given an n * m matrix grid where each element can either be 0 or 1. You need to find the shortest distance between a given source cell to a destination cell. The path can only be created out of a cell if its value is 1. 

If the path is not possible between the source cell and the destination cell, then return -1.

Note: You can move into an adjacent cell if that adjacent cell is filled with element 1. Two cells are adjacent if they share a side. In other words, you can move in one of four directions, Up, Down, Left, and Right.

Examples:

Example 1:

Input:
grid[][] = {{1, 1, 1, 1},
            {1, 1, 0, 1},
            {1, 1, 1, 1},
            {1, 1, 0, 0},
            {1, 0, 0, 1}}
source = {0, 1}
destination = {2, 2}
Output:
3

Explanation: 

1 1 1 1
1 1 0 1
1 1 1 1
1 1 0 0
1 0 0 1
The highlighted part in the above matrix denotes the shortest path from source to destination cell.

Example 2:

Input:
grid[][] = {{1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1},
            {1, 1, 1, 1, 0},
            {1, 0, 1, 0, 1}}
source = {0, 0}
destination = {3, 4}
Output:
-1 
Explanation: 
Since, there is no path possible between the source cell and the destination cell, hence we return -1.
'''
from typing import List
from collections import deque

class Solution:
  def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
    if grid[source[0]][source[1]] == 0 or grid[destination[0]][destination[1]] == 0:
      return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1, 0), (0, -1), (-1, 0)]

    queue = deque()
    queue.append((source[0], source[1], 0))

    visited = [[False] * cols for _ in range(rows)]
    visited[source[0]][source[1]] = True

    while queue:
      r, c, dist = queue.popleft()
      
      if [r, c] == destination:
        return dist
      
      for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
          visited[nr][nc] = True
          queue.append((nr, nc, dist + 1))

    return -1

if __name__ == "__main__":
  grid = [
      [1, 1, 1, 1],
      [1, 1, 0, 1],
      [1, 1, 1, 1],
      [1, 1, 0, 0],
      [1, 0, 0, 1]
  ]
  source = [0, 1]
  destination = [2, 2]

  sol = Solution()
  print(sol.shortestPath(grid, source, destination))
