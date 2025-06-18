# Non-overlapping Intervals -> Little bit tweaked from NMeetingsInOneRoom.py

'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
'''
from typing import List

# TC: O(N log N) + O(N)
# SC: O(1)
class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    n = len(intervals)
    intervals = sorted(intervals, key = lambda x: x[1])
    count = 1
    lastEndInterval = intervals[0][1]
    
    for i in range(1, n):
      if intervals[i][0] >= lastEndInterval:
        count += 1
        lastEndInterval = intervals[i][1]

    return n - count

if __name__ == "__main__":
  solution = Solution()
  intervals = [[1,2],[1,2],[1,2]]
  result = solution.eraseOverlapIntervals(intervals)
  print(result)