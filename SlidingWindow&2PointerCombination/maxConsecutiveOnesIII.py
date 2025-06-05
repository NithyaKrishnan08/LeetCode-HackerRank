# Maximum Consecutive Ones III

'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''
# This problem statement can be changed as -> Longest subarray with atmost K zeros
from typing import List

class Solution:
  # Brute force solution
  # T: O(N^2)
  # S: O(256)
  def longestOnes1(self, nums: List[int], k: int) -> int:
    max_len = 0
    for i in range(len(nums)):
      zeros_nums = 0
      for j in range(i, len(nums)):
        if nums[j] == 0:
          zeros_nums += 1
        
        if zeros_nums <= k:
          sub_length = j - i + 1
          max_len = max(max_len, sub_length)
        else:
          break
    
    return max_len
  
  # Optimal solution
  # T: O(N)
  # S: O(1)
  def longestOnes(self, nums: List[int], k: int) -> int:
    n = len(nums)
    max_len = 0
    zeros_nums = 0
    left, right = 0, 0
    while right < n:
      if nums[right] == 0:
        zeros_nums += 1
      if zeros_nums > k:
        if nums[left] == 0:
          zeros_nums -= 1
        left += 1
      if zeros_nums <= k:
        sub_len = right - left + 1
        max_len = max(max_len, sub_len)

      right += 1
    
    return max_len
  
if __name__ == "__main__":
  nums = [1,1,1,0,0,0,1,1,1,1,0]
  k = 2
  solution = Solution()
  result = solution.longestOnes(nums, k)
  print(result)
