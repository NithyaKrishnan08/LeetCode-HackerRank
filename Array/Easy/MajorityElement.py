# Majority Element
# https://leetcode.com/problems/majority-element/description/
# Difficulty: Easy

'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''

from typing import List
from collections import Counter

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    nums_map = Counter(nums)
    n = len(nums)

    for num, freq in nums_map.items():
      if freq > n // 2:
        return num

    return -1
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.majorityElement(nums = [3,2,3]))
  print(sol.majorityElement(nums = [2,2,1,1,1,2,2]))