# Subarrays with K Different Integers
# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
# Leetcode: 992
# Difficulty - Hard

'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
'''
from typing import List

class Solution:
  # Brute force solution
  # TC: O(N^2)
  # SC: O(N)
  def subarraysWithKDistinct1(self, nums: List[int], k: int) -> int:
    n = len(nums)
    sub_array_count = 0

    for i in range(n):
      mpp = {}
      for j in range(i, n):
        mpp[nums[j]] = mpp.get(nums[j], 0) + 1

        if len(mpp) == k:
          sub_array_count += 1
        elif len(mpp) > k:
          break
        
    return sub_array_count
  
  # Optimal solution
  # TC: O(2N)
  # SC: O(N)
  def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    def subarrayWithAtmostK(k):
      n = len(nums)
      sub_array_count = 0
      mpp = {}
      left = 0

      for right in range(n):
        mpp[nums[right]] = mpp.get(nums[right], 0) + 1

        while len(mpp) > k:
          mpp[nums[left]] -= 1
          if mpp[nums[left]] == 0:
            del mpp[nums[left]]
          left += 1

        sub_array_count = sub_array_count + (right - left + 1)
          
      return sub_array_count
    
    return subarrayWithAtmostK(k) - subarrayWithAtmostK(k - 1)
  
if __name__ == "__main__":
  nums = [1,2,1,2,3]
  k = 2
  solution = Solution()
  result = solution.subarraysWithKDistinct1(nums, k)
  print(result)
