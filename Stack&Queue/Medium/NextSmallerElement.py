# Next Smaller Element (NSE) for every element in the given array
# Difficulty: Medium

'''
Given an array arr[] of integers, find the Next Smaller Element (NSE) for each element in the array.

The Next Smaller Element of an element x is defined as the first element to the right of x in the array that is strictly smaller than x.
If no such element exists for a particular position, the NSE should be considered as -1.
Examples:

Input: arr[] = [4, 8, 5, 2, 25]
Output: [2, 5, 2, -1, -1]
Explanation: 
The first element smaller than 4 having index > 0 is 2.
The first element smaller than 8 having index > 1 is 5.
The first element smaller than 5 having index > 2 is 2.
There are no elements smaller than 2 having index > 3.
There are no elements smaller than 25 having index > 4.

Input: arr[] = [13, 7, 6, 12]
Output: [7, 6, -1, -1]
Explanation: 
The first element smaller than 13 having index > 0 is 7.
The first element smaller than 7 having index > 1 is 6.
There are no elements smaller than 6 having index > 2.
There are no elements smaller than 12 having index > 3.
'''

from typing import List

class Solution:
  # Optimal solution
  # TC: O(2N)
  # SC: O(N) + O(N)
  def nextSmallerElement(self, nums: List[int]) -> List[int]:
    n = len(nums)
    nextSmallerElement_arr = [-1] * n

    stack = []

    for i in range(n - 1, -1, -1):
      while stack and stack[-1] >= nums[i]:
        stack.pop()

      nextSmallerElement_arr[i] = -1 if not stack else stack[-1]
      
      stack.append(nums[i])

    return nextSmallerElement_arr
  
if __name__ == "__main__":
  nums = [4, 8, 5, 2, 25]
  solution = Solution()
  result = solution.nextSmallerElement(nums)
  print(result)