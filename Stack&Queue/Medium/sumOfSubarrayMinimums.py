# Sum of Subarray Minimums
# https://leetcode.com/problems/sum-of-subarray-minimums/description/
# Leetcode: 907
# Difficulty: Medium

'''
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104

'''
from typing import List

class Solution:
  # Brute force solution
  # TC: O(N^2)
  # SC: O(1)
  def sumSubarrayMins1(self, arr: List[int]) -> int:
    n = len(arr)
    min_total = 0
    MOD_TOTAL = 10**9 + 7
    for i in range(n):
      min_value = arr[i]
      for j in range(i, n):
        min_value = min(min_value, arr[j])
        min_total = (min_total + min_value) % MOD_TOTAL

    return min_total
  
  # Optimal solution
  # TC: O(N)
  # SC: O(1)
  def findNextSmallerElement(self, arr):
    n = len(arr)
    nse_arr = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
      while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()

      nse_arr[i] = n if not stack else stack[-1]

      stack.append(i)

    return nse_arr
  
  def findPreviousSmallerElement(self, arr):
    n = len(arr)
    pse_arr = [-1] * n
    stack = []

    for i in range(n):
      while stack and arr[stack[-1]] > arr[i]:
        stack.pop()

      pse_arr[i] = -1 if not stack else stack[-1]

      stack.append(i)

    return pse_arr

  def sumSubarrayMins(self, arr: List[int]) -> int:
    n = len(arr)
    nse_arr = self.findNextSmallerElement(arr)
    pse_arr = self.findPreviousSmallerElement(arr)

    min_total = 0
    MOD_TOTAL = 10**9 + 7

    for i in range(n):
      left = i - pse_arr[i]
      right = nse_arr[i] - i
      min_total = (min_total + (left * right * arr[i]) % MOD_TOTAL) % MOD_TOTAL

    return min_total
  
if __name__ == "__main__":
  arr = [3,1,2,4]
  solution = Solution()
  result = solution.sumSubarrayMins(arr)
  print(result)