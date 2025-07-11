# Remove K Digits

'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
'''

class Solution:
  def removeKdigits(self, num: str, k: int) -> str:
    stack = []
    for ch in num:
      # Remove larger elements from the stack if possible
      while stack and k > 0 and stack[-1] > ch:
        stack.pop()
        k -=1
      stack.append(ch)

    # k still remains
    while k > 0:
      stack.pop()
      k -= 1
    
    result = ''.join(stack).lstrip('0')
    
    return result if result else "0"

if __name__ == "__main__":
  num = "1432219"
  k = 3
  solution = Solution()
  result = solution.removeKdigits(num, k)
  print(result)
    
    

