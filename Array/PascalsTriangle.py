# Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/description/
# Leetcode: 118

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
    res = [[1]]

    for i in range(1, numRows):
      prev = res[-1]
      row = [1] # first element is always 1

      # For middle elements - there are no middle elements for row 1
      for j in range(1, i):
        row.append(prev[j - 1] + prev[j])
      row.append(1) # last element is always 1
      res.append(row)

    return res

if __name__ == '__main__':
  sol = Solution()
  print(sol.generate(5))
  print(sol.generate(1))
  print(sol.generate(2))  