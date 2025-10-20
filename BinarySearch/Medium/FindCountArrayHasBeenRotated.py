# Find out how many times the array has been rotated

'''
Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated. 

Example 1:
Input Format: arr = [4,5,6,7,0,1,2,3]
Result: 4
Explanation: The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.

Example 2:
Input Format: arr = [3,4,5,1,2]
Result: 3
Explanation: The original array should be [1,2,3,4,5]. So, we can notice that the array has been rotated 3 times.

'''
from typing import List

class Solution:
  def findNoOfRotation(self, nums):
    n = len(nums)
    low, high = 0, n - 1

    while low < high:
      mid = (low + high) // 2

      if nums[mid] > nums[high]:
        low = mid + 1
      else:
        high = mid

    return low
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.findNoOfRotation(nums = [4,5,6,7,0,1,2,3])) # 4
  print(sol.findNoOfRotation(nums = [3,4,5,1,2])) # 3
