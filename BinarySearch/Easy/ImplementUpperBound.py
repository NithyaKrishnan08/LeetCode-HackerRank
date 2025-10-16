# Implement Upper Bound

'''
The upper bound of a number x in a sorted array arr is the smallest index idx such that arr[idx] > x. If all elements in the array are less than or equal to x, the upper bound is n (the size of the array).
If the greater value does not exist then our answer is n, Where n is the size of the given array.

Example 1

Input:
arr = [1, 2, 4, 6, 8]
x = 5

Output:
Upper bound of 5 is at index 3

Example 2

Input:
arr = [1, 3, 5, 7, 9]
x = 2

Output:
Upper bound of 2 is at index 1
'''
from typing import List

class Solution:
  def upper_bound(self, arr: List[int], x: int) -> int:
    n = len(arr)
    ub = n
    left, right = 0, n - 1

    while left <= right:
      middle = (left + right) // 2

      if arr[middle] > x:
        ub = middle
        right = middle - 1
      else:
        left = middle + 1

    return ub
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.upper_bound(arr = [1, 2, 4, 6, 8], x = 5)) # 3
  print(sol.upper_bound(arr = [1, 3, 5, 7, 9], x = 2)) # 1