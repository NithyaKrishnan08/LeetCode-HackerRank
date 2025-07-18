# Insert Intervals

'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
'''
from typing import List

# TC: O(N)
# SC: O(N)
class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    n = len(intervals)
    result = []
    i = 0

    # Left side of the interval
    while i < n and intervals[i][1] < newInterval[0]:
      result.append(intervals[i])
      i += 1

    # Overlapping of the interval
    while i < n and intervals[i][0] <= newInterval[1]:
      newInterval[0] = min(newInterval[0], intervals[i][0])
      newInterval[1] = max(newInterval[1], intervals[i][1])
      i += 1

    result.append(newInterval)

    # Right side of the interval
    while i < n:
      result.append(intervals[i])
      i += 1

    return result

if __name__ == "__main__":
  solution = Solution()
  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
  newInterval = [4,8]
  result = solution.insert(intervals, newInterval)
  print(result)