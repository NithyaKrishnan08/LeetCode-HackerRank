# Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Leetcode: 4
# Difficulty: Hard

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
from typing import List

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
      nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m

    while low <= high:
      i = (low + high) // 2
      j = (m + n + 1) // 2 - i

      left1 = float('-inf') if i == 0 else nums1[i - 1]
      right1 = float('inf') if i == m else nums1[i]
      left2 = float('-inf') if j == 0 else nums2[j - 1]
      right2 = float('inf') if j == n else nums2[j]

      # Found correct partition
      if left1 <= right2 and left2 <= right1:
        if (m + n) % 2 == 0:
          return (max(left1, left2) + min(right1, right2)) / 2
        else:
          return max(left1, left2)

      elif left1 > right2:
        high = i - 1
      else:
        low = i + 1

    # Should never reach here
    return 0.0


if __name__ == '__main__':
  sol = Solution()
  print(sol.findMedianSortedArrays([1,3], [2]))       # 2.0
  print(sol.findMedianSortedArrays([1,2], [3,4]))     # 2.5