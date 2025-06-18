# N meetings in one room

'''

N meetings in one room


Problem Statement: There is one meeting room in a firm. You are given two arrays, start and end each of size N.For an index ‘i’, start[i] denotes the starting time of the ith meeting while end[i]  will denote the ending time of the ith meeting. Find the maximum number of meetings that can be accommodated if only one meeting can happen in the room at a  particular time. Print the order in which these meetings will be performed.

Example:

Input:  N = 6,  start[] = {1,3,0,5,8,5}, end[] =  {2,4,5,7,9,9}

Output: 1 2 4 5

Explanation: See the figure for a better understanding.
'''

from typing import List

class meeting:
  def __init__(self, start, end, position):
    self.start = start
    self.end = end
    self.position = position

# TC: O(N) + O(N log N) + O(N)
# SC: O(N)
class Solution:
  def maxMeetings(self, s: List[int], e: List[int], n: int) -> List[int]:
    meet = [meeting(s[i], e[i], i + 1) for i in range(n)]
    sorted(meet, key = lambda x: (x.end, x.position))
    answer = []
    limit = meet[0].end
    answer.append(meet[0].position)

    for i in range(n):
      if meet[i].start > limit:
        limit = meet[i].end
        answer.append(meet[i].position)

    return answer

if __name__ == "__main__":
  solution = Solution()
  n = 6
  start = [1, 3, 0, 5, 8, 5]
  end = [2, 4, 5, 7, 9, 9]
  result = solution.maxMeetings(start, end, n)
  print(result)    