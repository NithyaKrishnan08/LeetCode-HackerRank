# Flood Fill

'''
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

 

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:



From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation:

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
'''

from typing import List
from collections import deque

# TC: O(m * n)
# SC: O(m * n)

class Solution:
  # BFS Approach
  def floodFillBFS(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    # If original color is same as new color, do nothing and return the image
    if original_color == color:
      return image
    
    queue = deque()
    queue.append((sr, sc))
    image[sr][sc] = color

    # Directions for 4-directional adjacency -> down, up, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
      r, c = queue.popleft()
      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
          image[nr][nc] = color
          queue.append((nr, nc))


    return image
  
  # DFS Approach
  def floodFillDFS(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    # If original color is same as new color, do nothing and return the image
    if original_color == color:
      return image
    
    def dfs(r, c):
      if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
        return
      
      image[r][c] = color
      # Explore in all directions
      dfs(r - 1, c)
      dfs(r + 1, c)
      dfs(r, c - 1)
      dfs(r, c + 1)

    dfs(sr, sc)

    return image
  
if __name__ == "__main__":
  solution = Solution()
  image = [[1,1,1],[1,1,0],[1,0,1]]
  sr = 1
  sc = 1
  color = 2
  result1 = solution.floodFillBFS(image, sr, sc, color)
  print(result1)

  result2 = solution.floodFillDFS(image, sr, sc, color)
  print(result2)