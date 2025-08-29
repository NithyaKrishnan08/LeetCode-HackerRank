# Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/description/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
# Leetcode Problem 273: Integer to English Words

'''
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
'''

class Solution:
  def numberToWords(self, num: int) -> str:
    if num == 0:
      return "Zero"
    
    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                "Seventeen", "Eighteen", "Nineteen"]
    
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    thousands = ["", "Thousand", "Million", "Billion"]
    
    def helper(n):
      if n == 0:
        return ""
      elif n < 20:
        return below_20[n] + " "
      elif n < 100:
        return tens[n // 10] + " " + helper(n % 10)
      else:
        return below_20[n // 100] + " Hundred " + helper(n % 100)
    
    result = ""
    for i in range(len(thousands)):
      if num % 1000 != 0:
        result = helper(num % 1000) + thousands[i] + " " + result
      num //= 1000
    
    return result.strip()
  
if __name__ == "__main__":
  s = Solution()
  print(s.numberToWords(123))        # "One Hundred Twenty Three"
  print(s.numberToWords(12345))      # "Twelve Thousand Three Hundred Forty Five"
  print(s.numberToWords(1234567))    # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
  print(s.numberToWords(0))          # "Zero"
  print(s.numberToWords(1000010))    # "One Million Ten"
  print(s.numberToWords(1000000))    # "One Million"
  print(s.numberToWords(1000000000)) # "One Billion"
  print(s.numberToWords(1000000001)) # "One Billion One"
        