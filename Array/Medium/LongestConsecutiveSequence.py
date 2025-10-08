# Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Difficulty: Medium

'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
from typing import List

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
      return 0

    num_set = set(nums)
    longest_length = 0

    for num in num_set:
      if num - 1 not in num_set:
        curr_length = 1
        while num + curr_length in num_set:
          curr_length += 1
        longest_length = max(longest_length, curr_length)

    return longest_length
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.longestConsecutive(nums = [100,4,200,1,3,2])) # 4
  print(sol.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])) # 9
  print(sol.longestConsecutive(nums = [1,0,1,2])) # 3
        