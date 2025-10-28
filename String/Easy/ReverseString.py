# Reverse String
# https://leetcode.com/problems/reverse-string/description/
# Leetcode: 344
# Difficulty: Easy

'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
 

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
'''

from typing import List

class Solution:
  def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s)
    low, high = 0, n - 1
    while low <= high:
        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1
        

    return s
  
if __name__ == "__main__":
  char_array = ["h","e","l","l","o"]
  sol = Solution()
  result = sol.reverseString(char_array)
  print(result)