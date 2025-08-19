# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/
# Leetcode : 22

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
from typing import List

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    result = []

    def backtrack(current_str, open_count, close_count):
      if len(current_str) == 2 * n:
        result.append(current_str)
        return
      
      if open_count < n:
        backtrack(current_str + '(', open_count + 1, close_count)
      
      if close_count < open_count:
        backtrack(current_str + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result
  
if __name__ == "__main__":
  n = 3
  solution = Solution()
  result = solution.generateParenthesis(n)
  print(result)