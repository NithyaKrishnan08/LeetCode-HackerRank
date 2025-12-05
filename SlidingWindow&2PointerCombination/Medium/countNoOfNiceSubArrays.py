# count Number of Nice Subarrays
# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
# Leetcode: 1248
# Difficulty: Medium

'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16 

Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''

from typing import List

class Solution:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    def at_most_odd(k: int) -> int:
      n = len(nums)
      odd_count = 0
      nice_array_count = 0
      left, right = 0, 0

      while right < n:
        if nums[right] % 2 == 1:
          odd_count += 1
        
        while odd_count > k:
          if nums[left] % 2 == 1:
            odd_count -= 1
          left += 1
          
        nice_array_count += right - left + 1
        right += 1

      return nice_array_count
    
    return at_most_odd(k) - at_most_odd(k - 1)

if __name__ == "__main__":
  nums = [2,2,2,1,2,2,1,2,2,2]
  k = 2
  solution = Solution()
  result = solution.numberOfSubarrays(nums, k)
  print(result)