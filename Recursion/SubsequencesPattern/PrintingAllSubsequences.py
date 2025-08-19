# Print all subsequences
# A contigous/ non-contigous sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

# arr = [3, 1, 2]
# Subsequences: [], [3], [1], [2], [3, 1], [3, 2], [1, 2], [3, 1, 2]

'''
Problem Statement: Given an array, find all the possible subsequences of the array.

Examples:

Example 1:
Input: arr = [3, 1, 2]
Output: [], [3], [1], [2], [3, 1], [3, 2], [1, 2], [3, 1, 2]
Explanation: Printing all the subsequences for the array.
'''

class Solution:
  def printAllSubsequences(self, arr):
    n = len(arr)
    result = []

    def backtrack(idx, path):
      if idx >= n:
        result.append(path[:]) #Append the current subsequence
        return
      
      # Include the current element
      backtrack(idx + 1, path + [arr[idx]])

      # Exclude the current element
      backtrack(idx + 1, path)

    backtrack(0, [])
    
    return result

if __name__ == "__main__":
  sol = Solution()
  print(sol.printAllSubsequences([3, 1, 2]))
    
      
