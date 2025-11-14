# Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/description/
# Leetcode Problem 40: Combination Sum II
# Difficulty: Medium

'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''
from typing import List

class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    n = len(candidates)
    result = []

    def backtrack(start, path, current_sum):
      if current_sum == target:
        result.append(path[:])
        return
      
      # Pick the current element
      for i in range(start, n):
        if i > start and candidates[i] == candidates[i - 1]:
          continue #Skip duplicates at the same level

        if current_sum + candidates[i] > target:
          break  # Skip if the sum exceeds target
        
        path.append(candidates[i])
        backtrack(i + 1, path, current_sum + candidates[i])  # Allow the same element to be picked again
        path.pop()  # Backtrack

    backtrack(0, [], 0)
    return result
  
if __name__ == "__main__":
  sol = Solution()
  candidates = [10,1,2,7,6,1,5]
  target = 8
  print(sol.combinationSum2(candidates, target))  # Output: [[1, 1, 6],[1, 2, 5], [1, 7], [2, 6]]
  
  candidates = [2,5,2,1,2]
  target = 5
  print(sol.combinationSum2(candidates, target))  # Output: [[1,2,2],[5]]

        