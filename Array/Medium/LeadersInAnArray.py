# Leaders in an array
# Difficult: Medium

'''
Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.

Note: The rightmost element is always a leader.

Examples:

Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

Input: arr[] = [1, 2, 3, 4, 5, 2]
Output: [5 2]
Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.
'''

class Solution:
  def leaders(self, arr):
    result = []
    n = len(arr)

    max_right = arr[-1]
    result.append(max_right)

    for i in range(n - 2, -1, -1):
      if arr[i] > max_right:
        max_right = arr[i]
        result.append(max_right)

    result.reverse()

    return result
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.leaders(arr = [16, 17, 4, 3, 5, 2]))