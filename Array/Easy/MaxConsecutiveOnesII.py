# Max Consecutive Ones II

'''
You are given a binary array nums that contains only 0s and 1s. You need to find the maximum number of consecutive 1s that you can get if you are allowed to flip at most one 0 to 1.

For example, if you have the array [1, 0, 1, 1, 0], you can flip the first 0 to get [1, 1, 1, 1, 0], which gives you 4 consecutive 1s. Or you could flip the last 0 to get [1, 0, 1, 1, 1], which gives you 3 consecutive 1s. The maximum would be 4.

The key constraint is that you can flip at most one 0, meaning you can either flip exactly one 0 or flip no 0s at all. Your goal is to find the longest possible sequence of consecutive 1s after performing this operation optimally.
'''
from typing import List

class Solution:
  def findMaxConsecutiveOnesII(self, nums: List[int]) -> int:
    left = 0
    zero_count = 0

    for num in nums:
      zero_count += num ^ 1

      if zero_count > 1:
        zero_count -= 1
        left += 1

    return len(nums) - left
  
if __name__ == "__main__":
  solution = Solution()
  print(solution.findMaxConsecutiveOnesII([1, 0, 1, 1, 0]))