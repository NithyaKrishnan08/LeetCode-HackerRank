# Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/
# Leetcode: 56

'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)
    intervals.sort(key=lambda x: x[0])
    merged = []

    for i in range(n):
      if not merged or merged[-1][1] < intervals[i][0]:
        merged.append(intervals[i])
      else:
        merged[-1][1] = max(merged[-1][1], intervals[i][1])

    return merged
  
if __name__ == "__main__":
  solution = Solution()
  print(solution.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
  print(solution.merge([[1,4],[4,5]])) # [[1,5]]
  print(solution.merge([[4,7],[1,4]])) # [[1,7]]