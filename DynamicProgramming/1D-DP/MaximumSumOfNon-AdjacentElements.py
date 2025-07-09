# Maximum sum of non-adjacent elements

'''
Prroblem Statement:

Given an array of ‘N’  positive integers, we need to return the maximum sum of the subsequence such that no two elements of the subsequence are adjacent elements in the array.

Note: A subsequence of an array is a list with elements of the array where some elements are deleted ( or not deleted at all) and the elements should be in the same order in the subsequence as in the array.


'''
# Recursion
def maxSumNonAdjacent0(index, arr):
  if(index == 0):
    return arr[index]
  
  if index < 0:
    return 0
  
  pick = arr[index] + maxSumNonAdjacent0(index - 2, arr)
  not_pick = maxSumNonAdjacent0(index - 1, arr)
  
  result = max(pick, not_pick)
  return result

# Memoization - Top - Bottom
# Time Complexity: O(N)
# Space Complexity : O(2N)

# 1. Write in terms of index
# 2. Do all stuff on the indexes
# 3. Take the minimum of all the stuffs

def maxSumNonAdjacent1_util(index, arr, dp):
  if index == 0:
    return arr[index]
  
  if index < 0:
    return 0
  
  if dp[index] != -1:
    return dp[index]
  
  pick = arr[index] + maxSumNonAdjacent1_util(index - 2, arr, dp)
  not_pick = maxSumNonAdjacent1_util(index - 1, arr, dp)
  
  dp[index] = max(pick, not_pick)
  return dp[index]

def maxSumNonAdjacent1(arr):
  n = len(arr)
  dp = [-1] * n
  return maxSumNonAdjacent1_util(n - 1, arr, dp)

#  Tabulation - Bottom to Up
# Time Complexity: O(N)
# Space Complexity: O(N)
def maxSumNonAdjacent2_util(index, arr, dp):
  n = len(arr)
  if n == 0:
    return 0
  
  if n == 1:
    return 0
  
  dp[0] = arr[0]
  dp[1] = max(arr[0], arr[1])
  
  for i in range(2, n):
    pick = arr[i] + dp[i - 2]
    not_pick = dp[i - 1]
  
    dp[i] = max(pick, not_pick)

  return dp[n - 1]

def maxSumNonAdjacent2(arr):
  n = len(arr)
  dp = [-1] * n
  return maxSumNonAdjacent2_util(n - 1, arr, dp)

# Space Optimization
# Time Complexity: O(N)
# Space Complexity: O(1)
def maxSumNonAdjacent3(arr):
  n = len(arr)
  if n == 0:
    return 0
  
  if n == 1:
    return 0
  
  prev2_i = 0
  prev1_i = arr[0]
  
  for i in range(1, n):
    pick = arr[i]
    if i > 1:
      pick += prev2_i
   
    not_pick = prev1_i
    curr = max(pick, not_pick)
  
    prev2_i = prev1_i
    prev1_i = curr

  return prev1_i

if __name__ == "__main__":
  arr = [1, 2, 3, 1, 3, 5, 8, 1, 9]
  n = len(arr)
  
  # Recursion solution
  # result = maxSumNonAdjacent0(n - 1, arr)
  # print(result)

  # Memoization 
  # result = maxSumNonAdjacent1(arr)
  # print(result)

  # Tabulation 
  # result = maxSumNonAdjacent2(arr)
  # print(result)

  # Space Optimization 
  result = maxSumNonAdjacent3(arr)
  print(result)

  