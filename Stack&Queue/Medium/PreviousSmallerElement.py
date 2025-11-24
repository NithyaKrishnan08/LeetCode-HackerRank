# Previous Smallest Element
# Difficulty: Medium

from typing import List

class Solution:
  # Brute Force solution
  # TC: O(N^2)
  # SC: O(N)
  def previousSmallerElements1(self, nums: List[int]) -> List[int]:
    n = len(nums)
    prevSmallerElement_arr = [-1] * n

    for i in range(n):
      for j in range(i - 1, -1, -1):
        if nums[j] < nums[i]:
          prevSmallerElement_arr[i] = nums[j]
          break

    return prevSmallerElement_arr

  # Optimal solution
  # TC: O(2N)
  # SC: O(N) + O(N)
  def previousSmallerElements(self, nums: List[int]) -> List[int]:
    n = len(nums)
    prevSmallerElement_arr = [-1] * n

    stack = []

    for i in range(n):
      while stack and stack[-1] >= nums[i]:
        stack.pop()

      prevSmallerElement_arr[i] = -1 if not stack else stack[-1]
      
      stack.append(nums[i])

    return prevSmallerElement_arr
  
if __name__ == "__main__":
  nums = [4, 5, 2, 10, 8]
  solution = Solution()
  result = solution.previousSmallerElements(nums)
  print(result)