# Partition Array for Maximum Sum
# https://leetcode.com/problems/partition-array-for-maximum-sum/description/
# Leetcode: 1043

'''
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
'''
from typing import List

class Solution:
  # Recursion
  # Step 1: Express everything in terms of the index (start)
  # Step 2: Try every partition from that index(start)
  # Step 3: Take the best partition

  # Time Complexity: O(2^n)
  # Space Complexity: O(n)
  def maxSumAfterPartitioning0(self, arr: List[int], k: int) -> int:
    n = len(arr)

    def solve(i):
      if i >= n:
        return 0
      
      length = 0
      max_value = float('-inf')
      max_sum = float('-inf')

      for j in range(i, min(i + k , n)):
        length += 1
        max_value = max(max_value, arr[j])
        current_sum = max_value * length + solve(j + 1)
        max_sum = max(max_sum, current_sum)
        
      return max_sum
    
    return solve(0)
  
  # Memoization
  # Time Complexity: O(n) * O(k)
  # Space Complexity: O(n) + O(n) -> Auxillary stack space
  def maxSumAfterPartitioning1(self, arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [-1] * n

    def solve(i):
      if i >= n:
        return 0
      
      if dp[i] != -1:
        return dp[i]
      
      length = 0
      max_value = float('-inf')
      max_sum = float('-inf')

      for j in range(i, min(i + k , n)):
        length += 1
        max_value = max(max_value, arr[j])
        current_sum = max_value * length + solve(j + 1)
        max_sum = max(max_sum, current_sum)
        
      dp[i] = max_sum
      return dp[i]
    
    return solve(0)
  
  # Tabulation
  # Time Complexity: O(n) * O(k)
  # Space Complexity: O(n)
  def maxSumAfterPartitioning2(self, arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
      length = 0
      max_value = float('-inf')
      max_sum = float('-inf')

      for j in range(i, min(i + k , n)):
        length += 1
        max_value = max(max_value, arr[j])
        current_sum = max_value * length + dp[j + 1]
        max_sum = max(max_sum, current_sum)
        
      dp[i] = max_sum
    
    return dp[0]
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.maxSumAfterPartitioning2([1,15,7,9,2,5,10], 3))  # Output: 84
  print(sol.maxSumAfterPartitioning2([1,4,1,5,7,3,6,1,9,9,3], 4))  # Output: 83
  print(sol.maxSumAfterPartitioning2([1], 1))  # Output: 1