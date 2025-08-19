# Power Set - Print All Subsequences

'''
Problem Statement: Given a string, find all the possible subsequences of the string.

Examples:

Example 1:
Input: str = "abc"
Output: a ab abc ac b bc c
Explanation: Printing all the 7 subsequence for the string "abc".

Example 2:
Input: str = "aa"
Output: a a aa 
Explanation: Printing all the 3 subsequences for the string "aa"
'''

def printaLLSubsequences(idx, path, arr, result):
  if idx == len(arr):
    if path: # Only add non-empty subsequences (This is optional)
      result.append(path[:])
    return
  
  # Include the current idx element
  path.append(arr[idx])
  printaLLSubsequences(idx + 1, path, arr, result)

  # backtrack and exclude the current character
  path.pop()
  printaLLSubsequences(idx + 1, path, arr, result)

if __name__ == "__main__":
  arr = [3, 1, 2]
  result = []
  printaLLSubsequences(0, [], arr, result)
  print(result)
