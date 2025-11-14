# Power Set - Print All Subsequences
# https://leetcode.com/problems/subsets/description/
# Leetcode: 78
# Difficulty: Medium

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

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''

def printaLLSubsequences(idx, path, arr, result):
  if idx == len(arr):
    result.append(path[:])
    return
    # if path: # Only add non-empty subsequences (This is optional)
    #   result.append(path[:])
    # return
    
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
