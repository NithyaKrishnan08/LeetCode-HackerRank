# Largest Element in an Array

'''
Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.
Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest.
Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 106
Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
'''

class solution:
  def largestElement(self, arr):
    n = len(arr)
    max_element = arr[0]
    for i in range(1, n):
      if arr[i] > max_element:
        max_element = arr[i]
    return max_element
  
if __name__ == "__main__":
  arr = [1, 8, 7, 56, 90]
  obj = solution()
  result = obj.largestElement(arr)
  print(f"Largest element in the array {arr} is: {result}")