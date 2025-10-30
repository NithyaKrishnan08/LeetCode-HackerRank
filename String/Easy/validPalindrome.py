'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

from typing import List
from collections import Counter

# Optimal solution
# Time Complexity: O(n)
# Space Complexity: O(n)

def isPalindrome(s: str) -> bool:
  alphabets = ''.join(char.lower() for char in s if char.isalnum())
  if len(alphabets) == 0 or alphabets.strip() == "":
    return True
  
  left, right = 0, len(alphabets) - 1
  while left < right:
    if alphabets[left] != alphabets[right]:
      return False
    left += 1
    right -= 1

  return True

if __name__ == "__main__":
  s1 = "A man, a plan, a canal: Panama"
  s2 = "race a car"
  s3 = ""

  print("Optimal solution")
  result1 = isPalindrome(s1)
  result2 = isPalindrome(s2)
  result3 = isPalindrome(s3)
  
  if result1:
    print(f"{s1} is valid palindrome")
  else:
    print(f"{s1} is not valid palindrome")

  if result2:
    print(f"{s2} is valid palindrome")
  else:
    print(f"{s2} is not valid palindrome")

  if result3:
    print(f"{s3} is valid palindrome")
  else:
    print(f"{s3} is not valid palindrome")