# Maximum Length of Subarray With Positive Product
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/description/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
# Leetcode Problem 1567: Maximum Length of Subarray With Positive Product

'''
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

 

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

from typing import List

class Solution:
  def getMaxLen(self, nums: List[int]) -> int:
    pos = neg = 0
    ans = 0

    for x in nums:
      if x == 0:
        pos = neg = 0
      elif x > 0:
        pos += 1
        neg = neg + 1 if neg > 0 else 0
      else:
        new_pos = neg + 1 if neg > 0 else 0
        new_neg = pos + 1
        pos, neg = new_pos, new_neg
      ans = max(ans, pos)

    return ans

if __name__ == "__main__":
  s = Solution()
  print(s.getMaxLen([1,-2,-3,4]))          # 4
  print(s.getMaxLen([0,1,-2,-3,-4]))       # 3
  print(s.getMaxLen([-1,-2,-3,0,1]))       # 2
  print(s.getMaxLen([-1,2]))                # 1
  print(s.getMaxLen([1,2,3,5,-6,4,0,10]))   # 4    