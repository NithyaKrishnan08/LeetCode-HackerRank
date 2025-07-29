# Subset sum equals to target

'''
Problem statement
You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.
Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.
For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.

Constraints:
1 <= T <= 5
1 <= N <= 10^3
0 <= ARR[i] <= 10^9
0 <= K <= 10^3

Sample Input 1:
2
4 5
4 3 2 1
5 4
2 5 1 6 7
Sample Output 1:
true
false
Explanation For Sample Input 1:
In example 1, ‘ARR’ is {4,3,2,1} and ‘K’ = 5. There exist 2 subsets with sum = 5. These are {4,1} and {3,2}. Hence, return true.
In example 2, ‘ARR’ is {2,5,1,6,7} and ‘K’ = 4. There are no subsets with sum = 4. Hence, return false.
Sample Input 2:
2
4 4
6 1 2 1
5 6
1 7 2 9 10
Sample Output 2:
true
false
Explanation For Sample Input 2:
In example 1, ‘ARR’ is {6,1,2,1} and ‘K’ = 4. There exist 1 subset with sum = 4. That is {1,2,1}. Hence, return true.
In example 2, ‘ARR’ is {1,7,2,9,10} and ‘K’ = 6. There are no subsets with sum = 6. Hence, return false.

Hints:
1. Can you find every possible subset of ‘ARR’ and check if its sum is equal to ‘K’?
2. Can you use dynamic programming and use the previously calculated result to calculate the new result?
3. Try to use a recursive approach followed by memoization by including both index and sum we can form. 
'''
from typing import List
from collections import defaultdict

class Solution:
  # Step 1: Express (idx, target)
  # Step 2: Explre possibilities of that idx: a[idx] - part of the subsequence & a[idx] - not part of the subsequence
  # TC: O(2^N)
  # SC: O(N)
  def subsetSumEqualsTarget0(self, nums: List[int], k: int) -> bool:
    def count(i, target):
      if target == 0:
        return True
      if i < 0 or target < 0:
        return False
      
      not_take = count(i - 1, target)
      take = count(i - 1, target - nums[i]) if nums[i] <= target else False
      
      return take or not_take
    
    return count(len(nums) - 1, k)
  
  # def subsetSumCount0(self, nums: List[int], k: int) -> int:
  #   def count(i, target):
  #     if i == 0:
  #       if target == 0 and nums[0] == 0:
  #         return 2
  #       if target == 0 or nums[0] == target:
  #         return 1
  #       return 0
      
  #     not_take = count(i - 1, target)
  #     take = 0
  #     if nums[i] <= target:
  #       take = count(i - 1, target - nums[i])
      
  #     return take + not_take
    
  #   return count(len(nums) - 1, k)


  # Memoization approach
  # TC: O(n * k)
  # SC: O(n * k) + O(n) for recursion stack
  def subsetSumEqualsTarget1(self, nums: List[int], k: int) -> bool:
    n = len(nums)
    dp = [[-1 for _ in range(k + 1)] for _ in range(n)]

    def count(i, target):
      if target == 0:
        return True
      if i < 0 or target < 0:
        return False
      
      if dp[i][target] != -1:
        return dp[i][target]
      
      not_take = count(i - 1, target)
      take = count(i - 1, target - nums[i]) if nums[i] <= target else False
      
      dp[i][target] = take or not_take
      return dp[i][target]
    
    return count(n - 1, k)
  
  # Tabulation approach
  # TC: O(n * k)
  # SC: O(n * k)
  def subsetSumEqualsTarget2(self, nums: List[int], k: int) -> bool:
    n = len(nums)
    dp = [[False for _ in range(k + 1)] for _ in range(n)]

    # Target = 0 is always true
    for i in range(n):
      dp[i][0] = True
    # If first element is equal to target, then it is true
    if nums[0] <= k:
      dp[0][nums[0]] = True

    # Fill the dp table
    for i in range(1, n):
      for target in range(1, k + 1):
        not_take = dp[i - 1][target]
        take = dp[i - 1][target - nums[i]] if nums[i] <= target else False
        
        dp[i][target] = take or not_take

    return dp[n - 1][k]

if __name__ == "__main__":
  sol = Solution()
  nums = [1, 2, 3]
  k = 3

  # Recursive solution
  # result = sol.subsetSumEqualsTarget0(nums, k)
  # print(result)

  # Memoization solution
  # result = sol.subsetSumEqualsTarget1(nums, k)
  # print(result)

  # Tabulation solution
  result = sol.subsetSumEqualsTarget2(nums, k)
  print(result)