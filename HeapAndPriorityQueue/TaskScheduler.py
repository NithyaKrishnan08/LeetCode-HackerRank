# Task Scheduler
# https://leetcode.com/problems/task-scheduler/description/
# Leetcode: 621

'''
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

Constraints:
1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
'''

from typing import List
from collections import Counter, deque
import heapq

class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    # Each task takes 1 unit time
    # Minimize the idle time

    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()  # pairs of [-cnt, time]

    while maxHeap or q:
      time += 1

      if maxHeap:
        cnt = 1 + heapq.heappop(maxHeap)  # since we use -ve values
        if cnt:  # still some remaining
          q.append([cnt, time + n])  # add the cooling time

      if q and q[0][1] == time:  # cooling time is over
        heapq.heappush(maxHeap, q.popleft()[0])

    return time
  
if __name__ == '__main__':
  solver = Solution()
  tests = [
    (["A","A","A","B","B","B"], 2, 8),
    (["A","C","A","B","D","B"], 1, 6),
    (["A","A","A", "B","B","B"], 3, 10),
  ]
  for tasks, n, ans in tests:
    res = solver.leastInterval(tasks, n)
    print(f'tasks: {tasks}, n: {n} => ans: {ans}, res: {res}')
    assert res == ans