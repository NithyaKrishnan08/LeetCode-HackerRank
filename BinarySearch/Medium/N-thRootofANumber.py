# N-th root of a number

'''
Given two integers n and m, find the n-th root of m. The n-th root of m is an integer x such that x^n = m. If no such integer exists, return -1.

Examples: 

Input: n = 3, m = 27
Output: 3
Explanation: 33 = 27

Input: n = 3, m = 9
Output: -1
Explanation: 3rd root of 9 is not integer.
'''

class Solution:
  def nthRoot(self, n: int, m: int) -> int:
    low, high = 1, m
    
    while low <= high:
      mid = (low + high) // 2
      power = mid ** n
      
      if power == m:
          return mid
      elif power < m:
          low = mid + 1
      else:
          high = mid - 1
            
    return -1
  
if __name__ == "__main__":
  n = 3
  m = 27
  solution = Solution()
  print(solution.nthRoot(n, m))  # Output: 3