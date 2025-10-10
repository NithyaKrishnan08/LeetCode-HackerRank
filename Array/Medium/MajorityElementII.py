# Majority Element II
# https://leetcode.com/problems/majority-element-ii/description/
# Difficulty: Medium

# Boyer–Moore Voting Algorithm

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
'''

from typing import List
from collections import Counter

class Solution:
  def majorityElement1(self, nums: List[int]) -> List[int]:
    nums_map = Counter(nums)
    n = len(nums)
    result = []

    for num, freq in nums_map.items():
      if freq > n // 3:
        result.append(num)

    return result
  
  # Optimal solution
  def majorityElement(self, nums: List[int]) -> List[int]:
    if not nums:
      return []
    
    cand1 = cand2 = None
    count1 = count2 = 0

    for num in nums:
      if num == cand1:
        count1+= 1
      elif num == cand2:
        count2 += 1
      elif count1 == 0:
        cand1, count1 = num, 1
      elif count2 == 0:
        cand2, count2 = num, 1
      else:
        count1 -= 1
        count2 -= 1

    result = []
    for c in [cand1, cand2]:
      if nums.count(c) > len(nums) // 3:
        result.append(c)

    return result
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.majorityElement(nums = [3,2,3]))
  print(sol.majorityElement(nums = [1]))
  print(sol.majorityElement(nums = [1,2]))