# Subset Sum I


'''
Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.

Examples:

Example 1:

Input: N = 3, arr[] = {5,2,1}

Output: 0,1,2,3,5,6,7,8

Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8


Input: N=3,arr[]= {3,1,2}

Output: 0,1,2,3,3,4,5,6

Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [3], [3,1], [3,2]. [3,2,1],so the sums we get will be  0,1,2,3,3,4,5,6

'''
from typing import List

class Solution:
  def subsetSum(self, arr: List[int]) -> List[List[int]]:
    n = len(arr)
    result = []

    def backtrack(start, sum):
      if start == n:
        result.append(sum)
        return
      
      # Exclude the current element
      backtrack(start + 1, sum)
      
      # Include the current element
      backtrack(start + 1, sum + arr[start])

    backtrack(0, 0)
    return sorted(result)
  
if __name__ == "__main__":
  sol = Solution()
  arr = [5,2,1]
  print(sol.subsetSum(arr))  # Output: 0,1,2,3,5,6,7,8
  
  arr = [3,1,2]
  print(sol.subsetSum(arr))  # Output: 0,1,2,3,3,4,5,6

        