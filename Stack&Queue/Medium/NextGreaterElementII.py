# Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/description/
# Leetcode: 503
# Difficulty: Medium

'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
'''
from typing import List

class Solution:
  # Brute Force solution
  # TC: O(N^2)
  # SC: O(N)
  def nextGreaterElements1(self, nums: List[int]) -> List[int]:
    n = len(nums)
    nge_arr = [-1] * n

    for i in range(n):
      for j in range(i + 1, i + n, 1):
        idx = j % n
        if nums[idx] > nums[i]:
          nge_arr[i] = nums[idx]
          break

    return nge_arr

  # Optimal solution
  # TC: O(4N)
  # SC: O(2N)
  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    n = len(nums)
    nge_arr = [-1] * n

    stack = []
    for i in range(2 * n - 1, -1, -1):
      while stack and stack[-1] <= nums[i % n]:
        stack.pop()

      if (i < n):
        nge_arr[i] = -1 if not stack else stack[-1]
      
      stack.append(nums[i % n])

    return nge_arr
  
if __name__ == "__main__":
  nums = [1,2,3,4,3]
  solution = Solution()
  result = solution.nextGreaterElements(nums)
  print(result)