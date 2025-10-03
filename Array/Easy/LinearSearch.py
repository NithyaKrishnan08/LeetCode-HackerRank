# Linear Search

'''
roblem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

Examples:

Example 1:
Input: arr[]= 1 2 3 4 5, num = 3
Output: 2
Explanation: 3 is present in the 2nd index

Example 2:
Input: arr[]= 5 4 3 2 1, num = 5
Output: 0
Explanation: 5 is present in the 0th index
'''

from typing import List

class Solution:
  def linearSearch(self, arr: List[int], num: int) -> int:
    for i in range(len(arr)):
      if arr[i] == num:
        return i
    return -1
  
if __name__ == '__main__':
  solver = Solution()
  arr = [1, 2, 3, 4, 5]
  num = 3
  print(solver.linearSearch(arr, num))  # 2
  
  arr = [5, 4, 3, 2, 1]
  num = 5
  print(solver.linearSearch(arr, num))  # 0
  
  arr = [1, 2, 3, 4, 5]
  num = 6
  print(solver.linearSearch(arr, num))  # -1