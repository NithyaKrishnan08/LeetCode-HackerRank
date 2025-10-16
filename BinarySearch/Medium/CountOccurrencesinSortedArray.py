# Count Occurrences in Sorted Array

'''
Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

Examples

Example 1:
Input: N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
Output: 4
Explanation: 3 is occurring 4 times in 
the given array so it is our answer.

Example 2:
Input: N = 8,  X = 2 , array[] = {1, 1, 2, 2, 2, 2, 2, 3}
Output: 5
Explanation: 2 is occurring 5 times in the given array so it is our answer.
'''

class Solution:
  def findOccurences(self, arr, x):
    n = len(arr)

    def firstOccurence(arr, x):
      low, high = 0, n - 1
      first = -1

      while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
          first = mid
          high = mid - 1
        elif arr[mid] < x:
          low = mid + 1
        else:
          high = mid - 1

      return first
    
    def lastOccurence(arr, x):
      low, high = 0, n - 1
      last = -1

      while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
          last = mid
          low = mid + 1
        elif arr[mid] < x:
          low = mid + 1
        else:
          high = mid - 1

      return last
    
    first = firstOccurence(arr, x)
    last = lastOccurence(arr, x)

    return last - first + 1
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.findOccurences(arr = [2, 2 , 3 , 3 , 3 , 3 , 4], x = 3)) # 4
  print(sol.findOccurences(arr = [1, 1, 2, 2, 2, 2, 2, 3], x = 2)) # 5