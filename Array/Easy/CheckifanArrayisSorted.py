# Check if an Array is Sorted

'''
Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

Examples: 

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.

Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.
'''

class Solution:
  def isSorted(self, arr):
    n = len(arr)
    for i in range(1, n):
      if arr[i] < arr[i - 1]:
        return False
    return True
  
if __name__ == "__main__":
  arr = [10, 20, 30, 40, 50]
  obj = Solution()
  result = obj.isSorted(arr)
  print(f"The array {arr} is sorted: {result}")