# Path with minimum effort
# https://leetcode.com/problems/path-with-minimum-effort/description/

'''
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
'''
from typing import List
import heapq

# TC: O(M * N * log(M*N))
# sC: O(M * N)

class Solution:
  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    rows, cols = len(heights), len(heights[0])
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    effort = [[float('inf')] * cols for _ in range(rows)]
    effort[0][0] = 0

    min_heap = [(0, 0, 0)]

    while min_heap:
      current_effort, r, c = heapq.heappop(min_heap)

      if r == rows - 1 and c == cols - 1:
        return current_effort
      
      for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
          diff = abs(heights[nr][nc] - heights[r][c])
          new_effort = max(current_effort, diff)

          if new_effort < effort[nr][nc]:
            effort[nr][nc] = new_effort
            heapq.heappush(min_heap, (new_effort, nr, nc)) 

    return -1
  
if __name__ == "__main__":
  heights = [[1,2,2],[3,8,2],[5,3,5]]

  sol = Solution()
  print(sol.minimumEffortPath(heights))