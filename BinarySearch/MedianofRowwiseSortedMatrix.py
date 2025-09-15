# Median of Row-wise Sorted Matrix
# https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/description/
# Leetcode: 378

'''
Problem Statement: Given a row-wise sorted matrix of size MXN, where M is no. of rows and N is no. of columns, find the median in the given matrix.

Note: MXN is odd.

Example 1:
Input Format:M = 3, N = 3, matrix[][] =
1 4 9 
2 5 6
3 8 7
Result: 5

Explanation:  If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. So, median = 5

Example 2:
Input Format:M = 3, N = 3, matrix[][] =
1 3 8 
2 3 4
1 2 5
Result: 3

Explanation:  If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 7 8. So, median = 3
'''
import bisect

class Solution:
  # Brute force solution
  # Time Complexity: O(M*N log(M*N))
  # Space Complexity: O(M*N)
  def medianBrute(self, matrix):
    m = len(matrix)
    n = len(matrix[0])

    lst = []
    for i in range(m):
      for j in range(n):
        lst.append(matrix[i][j])

    lst.sort()
    median = lst[(m * n) // 2]
    return median
  
  # Optimal solution
  # Time Complexity: O(M*N log(M*N))
  # Space Complexity: O(M*N)

  def findElementsLessThanMid(self, matrix, mid):
    count = 0
    for row in matrix:
        count += bisect.bisect_right(row, mid)
    return count
  
  def median(self, matrix):
    m = len(matrix)
    n = len(matrix[0])

    required = (m * n) // 2

    low = min(matrix[i][0] for i in range(m))
    high = max(matrix[i][n - 1] for i in range(m))

    while low <= high:
      mid = (low + high) // 2
      smallerEquals = self.findElementsLessThanMid(matrix, mid)

      if smallerEquals <= required:
        low = mid + 1
      else:
        high = mid - 1

    return low

  
if __name__ == "__main__":
  matrix = [
    [1, 4, 9],
    [2, 5, 6],
    [3, 8, 7]
  ]

  solution = Solution()
  result = solution.medianBrute(matrix)
  print(result)

  result = solution.median(matrix)
  print(result)