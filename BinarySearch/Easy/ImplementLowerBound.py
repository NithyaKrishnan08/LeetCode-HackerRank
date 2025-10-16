# Implement Lower Bound

'''
The lower bound of a number x in a sorted array arr is the smallest index idx such that arr[idx] >= x. If all elements in the array are less than x, the lower bound is n (the size of the array).
If all numbers are smaller than x, then n should be the lower_bound of x, where n is the size of the given array.

Example 1
Input:
arr = [1, 3, 5, 7, 9]
x = 6
Output:
Lower bound of 6 is at index 3

Example 2
Input:
arr = [2, 4, 6, 8, 10]
x = 12
Output:
Lower bound of 12 is at index 5
'''
from typing import List

class Solution:
  def lower_bound(self, arr: List[int], x: int) -> int:
    n = len(arr)
    lb = n
    left, right = 0, n - 1

    while left <= right:
      middle = (left + right) // 2

      if arr[middle] >= x:
        lb = middle
        right = middle - 1
      else:
        left = middle + 1

    return lb
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.lower_bound(arr = [1, 3, 5, 7, 9], x = 6)) # 3
  print(sol.lower_bound(arr = [2, 4, 6, 8, 10], x = 12)) # 5