# Left Rotate Array
# Difficulty: Medium

'''
Given an integer array nums, rotate the array to the left by k steps, where k is non-negative.

 

Example 1:

Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
'''
from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n

    def reverse(i, j):
      while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    reverse(0, k - 1)
    reverse(k, n - 1)
    reverse(0, n - 1)
    

if __name__ == "__main__":
  s = Solution()
  arr = [3,7,8,9,10,11]
  k = 3
  s.rotate(arr, k)
  print(arr)  # [9, 10, 11, 3, 7, 8]
      