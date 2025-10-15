# Count the Number of Inversions
# https://leetcode.com/problems/count-the-number-of-inversions/description/
# Leetcode: 3193
# Difficulty: Hard

'''
You are given an integer n and a 2D array requirements, where requirements[i] = [endi, cnti] represents the end index and the inversion count of each requirement.

A pair of indices (i, j) from an integer array nums is called an inversion if:

i < j and nums[i] > nums[j]
Return the number of permutations perm of [0, 1, 2, ..., n - 1] such that for all requirements[i], perm[0..endi] has exactly cnti inversions.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, requirements = [[2,2],[0,0]]

Output: 2

Explanation:

The two permutations are:

[2, 0, 1]
Prefix [2, 0, 1] has inversions (0, 1) and (0, 2).
Prefix [2] has 0 inversions.
[1, 2, 0]
Prefix [1, 2, 0] has inversions (0, 2) and (1, 2).
Prefix [1] has 0 inversions.
Example 2:

Input: n = 3, requirements = [[2,2],[1,1],[0,0]]

Output: 1

Explanation:

The only satisfying permutation is [2, 0, 1]:

Prefix [2, 0, 1] has inversions (0, 1) and (0, 2).
Prefix [2, 0] has an inversion (0, 1).
Prefix [2] has 0 inversions.
Example 3:

Input: n = 2, requirements = [[0,0],[1,0]]

Output: 1

Explanation:

The only satisfying permutation is [0, 1]:

Prefix [0] has 0 inversions.
Prefix [0, 1] has an inversion (0, 1).
 

Constraints:

2 <= n <= 300
1 <= requirements.length <= n
requirements[i] = [endi, cnti]
0 <= endi <= n - 1
0 <= cnti <= 400
The input is generated such that there is at least one i such that endi == n - 1.
The input is generated such that all endi are unique.
'''

from typing import List

class Solution:
  def countInversions(self, nums: List[int]) -> int:
    def merge_sort(arr, temp, left, right):
      inv_count = 0
      if left < right:
        mid = (left + right) // 2

        # Count inversions in left half
        inv_count += merge_sort(arr, temp, left, mid)
        # Count inversions in right half
        inv_count += merge_sort(arr, temp, mid + 1, right)
        # Count cross-inversions while merging
        inv_count += merge(arr, temp, left, mid, right)
      return inv_count

    def merge(arr, temp, left, mid, right):
      i, j, k = left, mid + 1, left
      inv_count = 0

      while i <= mid and j <= right:
          if arr[i] <= arr[j]:
              temp[k] = arr[i]
              i += 1
          else:
              temp[k] = arr[j]
              j += 1
              inv_count += (mid - i + 1)  # all remaining in left > arr[j]
          k += 1

      # Copy remaining elements
      while i <= mid:
          temp[k] = arr[i]
          i += 1
          k += 1

      while j <= right:
          temp[k] = arr[j]
          j += 1
          k += 1

      # Copy back to original array
      for i in range(left, right + 1):
          arr[i] = temp[i]

      return inv_count

    n = len(nums)
    temp = [0] * n
    return merge_sort(nums, temp, 0, n - 1)
  
if __name__ == "__main__":
  solution = Solution()
  nums = [2, 3, 8, 6, 1]
  print("Number of inversions are:", solution.countInversions(nums))
  nums = [1, 20, 6, 4, 5]
  print("Number of inversions are:", solution.countInversions(nums))
  nums = [5, 4, 3, 2, 1]
  print("Number of inversions are:", solution.countInversions(nums))

