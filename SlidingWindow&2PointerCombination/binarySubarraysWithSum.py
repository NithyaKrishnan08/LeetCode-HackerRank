# Binary Subarrays With Sum
'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
'''
from typing import List

class Solution:
  # Brute force solution
  # T: O(N^2)
  # S: O(1)
  def numSubarraysWithSum1(self, nums: List[int], goal: int) -> int:
    n = len(nums)
    sub_arr_count = 0
    for i in range(n):
      sum = 0
      for j in range(i, n):
        sum += nums[j]
        if sum == goal:
          sub_arr_count += 1
        elif sum > goal:
          sum = 0
          break

    return sub_arr_count
  
  # Optimal solution
  # T: O(2 * 2N)
  # S: O(1)
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    def at_most(k: int) -> int:
      n = len(nums)
      if k < 0:
        return 0
      
      sub_arr_count = 0
      left, right = 0, 0

      sum = 0
      while right < n:
        sum += nums[right]

        while sum > k:
          sum -= nums[left]
          left += 1
        
        sub_arr_count = sub_arr_count + (right - left + 1)
        right += 1

      return sub_arr_count
    
    return at_most(goal) - at_most(goal - 1)
  

if __name__ == "__main__":
  nums = [1,0,1,0,1]
  goal = 2

  solution = Solution()
  result = solution.numSubarraysWithSum(nums, goal)
  print(result)
        
