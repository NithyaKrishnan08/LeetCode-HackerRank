# Trapping Rain Water

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''
from typing import List

class Solution:
  # Better solution
  # TC: O(2N) + O(N) -> O(3N)
  # SC: O(2N)
  def trap1(self, height: List[int]) -> int:
    n = len(height)
    if n <= 2:
      return 0
    
    total_water = 0

    def prefixMax(height):
      prefix_max = [0] * n
      prefix_max[0] = height[0]

      for i in range(1, n):
        prefix_max[i] = max(prefix_max[i - 1], height[i])

      return prefix_max
    
    def suffixMax(height):
      suffix_max = [0] * n
      suffix_max[n - 1] = height[n - 1]

      for i in range(n - 2, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1], height[i])

      return suffix_max

    prefix_max = prefixMax(height)
    suffix_max = suffixMax(height)

    for i in range(n):
      leftMax = prefix_max[i]
      rightMax = suffix_max[i]
      if height[i] < leftMax and height[i] < rightMax:
        total_water += min(leftMax, rightMax) - height[i]

    return total_water
  
  # Optimal solution
  # TC: O(N)
  # SC: O(1)
  def trap(self, height: List[int]) -> int:
    n = len(height)
    if n <= 2:
      return 0
    
    total_water = 0
    leftMax, rightMax = 0, 0
    left, right = 0, n - 1

    while left < right:
      if height[left] <= height[right]:
        if leftMax > height[left]:
          total_water += leftMax - height[left]
        else:
          leftMax = height[left]
        
        left += 1
      else:
        if rightMax > height[right]:
          total_water += rightMax - height[right]
        else:
          rightMax = height[right]
        
        right -= 1

    return total_water
  
if __name__ == "__main__":
  height = [0,1,0,2,1,0,1,3,2,1,2,1]
  solution = Solution()
  result = solution.trap(height)
  print(result)