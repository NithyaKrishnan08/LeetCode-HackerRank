# Partition a Set into Two Subsets With Minimum Absolute Sum Difference
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/

'''
Problem statement
You are given an array 'arr' containing 'n' non-negative integers.

Your task is to partition this array into two subsets such that the absolute difference between subset sums is minimum.

You just need to find the minimum absolute difference considering any valid division of the array elements.

Note:
1. Each array element should belong to exactly one of the subsets.

2. Subsets need not always be contiguous.
For example, for the array : [1, 2, 3], some of the possible divisions are 
   a) {1,2} and {3}
   b) {1,3} and {2}.

3. Subset-sum is the sum of all the elements in that subset. 
Example:
Input: 'n' = 5, 'arr' = [3, 1, 5, 2, 8].

Ouput: 1

Explanation: We can partition the given array into {3, 1, 5} and {2, 8}. 
This will give us the minimum possible absolute difference i.e. (10 - 9 = 1).

Sample Input 1:
4
1 2 3 4
Sample Output 1:
0
Explanation for sample input 1:
We can partition the given array into {2,3} and {1,4}.
This will give us the minimum possible absolute difference i.e. (5 - 5 = 0) in this case.
Sample Input 2:
3
8 6 5
Sample Output 2:
3
Explanation for sample input 2:
We can partition the given array into {8} and {6,5}. 
This will give us the minimum possible absolute difference i.e. (11 - 8 = 3).
Expected time complexity:
The expected time complexity is O(n * 𝚺 'arr'[i]), where 𝚺 'arr'[i] denotes the sum of all elements in 'arr'.
Constraints:
1 <= 'n' <= 10^3
0 <= 'arr'[i] <= 10^3
0 <= 𝚺 'arr'[i] <= 10^4, 

where 𝚺 'arr'[i] denotes the sum of all elements in 'arr'.
'''

from typing import List

def minSubsetSumDifference(arr: List[int], n: int) -> int:
  total_sum = sum(arr)
  
  # Initialize DP table
  dp = [[False] * (total_sum + 1) for _ in range(n + 1)]
  
  # Base case: 0 sum is always possible
  for i in range(n + 1):
    dp[i][0] = True

  # Fill the DP table
  for i in range(1, n + 1):
    for j in range(0, total_sum + 1):
      if arr[i - 1] <= j:
        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
      else:
        dp[i][j] = dp[i - 1][j]

  # Find the minimum difference
  min_diff = float('inf')
  for j in range(total_sum // 2, -1, -1):
    if dp[n][j]:
      min_diff = total_sum - 2 * j
      break

  return min_diff

print(minSubsetSumDifference([3, 1, 5, 2, 8], 5))  # Output: 1
print(minSubsetSumDifference([1, 2, 3, 4], 4))     # Output: 0
print(minSubsetSumDifference([8, 6, 5], 3))  