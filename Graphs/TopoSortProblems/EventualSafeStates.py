# Find Eventual Safe States in a Directed Graph
# https://leetcode.com/problems/find-eventual-safe-states/description/

'''
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

 

Example 1:

Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
 

Constraints:

n == graph.length
1 <= n <= 104
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 104].
'''
from collections import defaultdict, deque
from typing import List

# TC: O(V + E)
# SC: O(V + E)

class Solution:
  def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    n = len(graph)
    out_degree = [0] * n
    reverse_graph = defaultdict(list)

    # Build reverse graph and out_degree array
    for u in range(n):
      for v in graph[u]:
        reverse_graph[v].append(u)
        out_degree[u] += 1

    # Queue for nodes with no outgoing nodes (terminal nodes)
    queue = deque()
    queue.extend([i for i in range(n) if out_degree[i] == 0])

    safe_nodes = [False] * n

    while queue:
      node = queue.popleft()
      safe_nodes[node] = True

      for prev in reverse_graph[node]:
        out_degree[prev] -= 1
        if out_degree[prev] == 0:
          queue.append(prev)

    return [i for i in range(n) if safe_nodes[i]]
  
if __name__ == "__main__":
  graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
  sol = Solution()
  print(sol.eventualSafeNodes(graph))