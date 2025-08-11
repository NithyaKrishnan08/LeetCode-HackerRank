# Longest Bitonic Subsequence

'''
Given an array arr[] containing n positive integers, a subsequence of numbers is called bitonic if it is first strictly increasing, then strictly decreasing. The task is to find the length of the longest bitonic subsequence. 
Note: Only strictly increasing (no decreasing part) or a strictly decreasing sequence should not be considered as a bitonic sequence.

Examples:

Input: arr[]= [12, 11, 40, 5, 3, 1]
Output: 5 
Explanation: The Longest Bitonic Subsequence is {12, 40, 5, 3, 1} which is of length 5.

Input: arr[] = [80, 60, 30]
Output: 0
Explanation: There is no possible Bitonic Subsequence.
'''

class Solution:
  # TC: 
  # SC: 
  def longestBitonicSeq(self, arr) -> int:
    n = len(arr)
    dp1 = [1] * (n) # LIS from left
    dp2 = [1] * (n) # LIS from right

    # Filling dp1 array - Increasing subsequence - forward direction
    for i in range(n):
      for j in range(i):
        if arr[i] > arr[j] and 1 + dp1[j] > dp1[i]:
          dp1[i] = 1 + dp1[j]

    # Filling dp2 array - Increasing subsequence - backward direction
    for i in range(n - 1, -1, -1):
      for j in range(n - 1, i, -1):
        if arr[i] > arr[j] and 1 + dp2[j] > dp2[i]:
          dp2[i] = 1 + dp2[j]

    # Finding longest bitonic array
    bitonic_len = 0
    for i in range(n):
      if dp1[i] > 1 and dp2[i] > 1:
        bitonic_len = max(bitonic_len, dp1[i] + dp2[i] - 1)

    return bitonic_len
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.longestBitonicSeq(arr = [12, 11, 40, 5, 3, 1])) # 5