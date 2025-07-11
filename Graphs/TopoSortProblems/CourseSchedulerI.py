# course Scheduler I
# https://leetcode.com/problems/course-schedule/

'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''

from typing import List
from collections import defaultdict, deque

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for dest, src in prerequisites:
      graph[src].append(dest)
      in_degree[dest] += 1

    queue = deque()
    for i in range(numCourses):
      if in_degree[i] == 0:
        queue.append(i)

    topological_order = []

    while queue:
      node = queue.popleft()
      topological_order.append(node)

      for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
          queue.append(neighbor)

    return len(topological_order) == numCourses
  
if __name__ == "__main__":
  numCourses = 2
  prerequisites = [[1,0],[0,1]]
  sol = Solution()
  print(sol.canFinish(numCourses, prerequisites))
