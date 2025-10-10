# Pascals Triangle
# https://leetcode.com/problems/pascals-triangle/description/
# Difficult: Easy

'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''

from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    result = [[1]]

    for i in range(1, numRows):
      prev = result[-1]
      row = [1]

      for j in range(1, i):
        row.append(prev[j - 1] + prev[j])

      row.append(1)
      result.append(row)

    return result
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.generate(numRows = 5))
  print(sol.generate(numRows = 1))