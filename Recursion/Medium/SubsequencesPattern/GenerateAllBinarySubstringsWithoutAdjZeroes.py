# Generate Binary Strings Without Adjacent Zeros
# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/
# Leetcode: 3211
# Difficulty: Medium

'''
You are given a positive integer n.

A binary string x is valid if all substrings of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.

 

Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:

Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".

Constraints:

1 <= n <= 18
'''
from typing import List

class Solution:
  def validStrings(self, n: int) -> List[str]:
    result = []

    def backtrack(current_string, last_char):
      if len(current_string) == N:
        result.append(current_string)
        return
      
      backtrack(current_string + '1', '1')
      
      if last_char != '0':
        backtrack(current_string + '0', '0')

    backtrack('', '')
    return result
  
if __name__ == "__main__":
  N = 3
  solution = Solution()
  result = solution.validStrings(N)
  print(result)

