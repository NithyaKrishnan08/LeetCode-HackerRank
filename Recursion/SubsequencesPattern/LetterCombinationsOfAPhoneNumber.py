# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Leetcode Problem 17: Letter Combinations of a Phone Number

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''
from typing import List

class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    n = len(digits)

    if n == 0:
      return []
    
    result = []

    digit_to_char = {
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz'
    }

    def backtrack(start, path):
      if len(path) == n:
        result.append(''.join(path))
        return
      
      for i in range(start, n):
        chars = digit_to_char[digits[i]]
        for char in chars:
          path.append(char)
          backtrack(i + 1, path)
          path.pop()
          
    backtrack(0, [])
    return result
  
if __name__ == "__main__":
  sol = Solution()
  digits = "23"
  print(sol.letterCombinations(digits))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
  
  digits = ""
  print(sol.letterCombinations(digits))  # Output: []
  
  digits = "2"
  print(sol.letterCombinations(digits))  # Output: ["a","b","c"]

  digits = "2345"
  print(sol.letterCombinations(digits))

      
      
        