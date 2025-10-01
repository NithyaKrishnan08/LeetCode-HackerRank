# Maximum Sum Combination
# Difficulty: Medium

'''
You are given two integer arrays a[] and b[] of equal size. A sum combination is formed by adding one element from a[] and one from b[], using each index pair (i, j) at most once. Return the top k maximum sum combinations, sorted in non-increasing order.

Examples:

Input: a[] = [3, 2], b[] = [1, 4], k = 2
Output: [7, 6]
Explanation: Possible sums: 3 + 1 = 4, 3 + 4 = 7, 2 + 1 = 3, 2 + 4 = 6, Top 2 sums are 7 and 6.
Input: a[] = [1, 4, 2, 3], b[] = [2, 5, 1, 6], k = 3
Output: [10, 9, 9]
Explanation: The top 3 maximum possible sums are : 4 + 6 = 10, 3 + 6 = 9, and 4 + 5 = 9
Constraints:
1 ≤ a.size() = b.size() ≤ 105
1 ≤ k ≤ a.size()
1 ≤ a[i], b[i] ≤ 104
'''
import heapq

class Solution:
  def maxCombinations(self, a, b, k):
    n = len(a)
    a.sort(reverse=True)
    b.sort(reverse=True)

    max_heap = []
    visited = set()

    heapq.heappush(max_heap, (-(a[0] + b[0]), 0, 0))
    visited.add((0, 0))

    result = []

    while k > 0 and max_heap:
      curr_sum, i, j = heapq.heappop(max_heap)
      result.append(-curr_sum)
      k -= 1

      if i + 1 < n and (i + 1, j) not in visited:
        heapq.heappush(max_heap, (-(a[i + 1] + b[j]), i + 1, j))
        visited.add((i + 1, j))

      if j + 1 < n and (i, j + 1) not in visited:
        heapq.heappush(max_heap, (-(a[i] + b[j + 1]), i, j + 1))
        visited.add((i, j + 1))

    return result
  
if __name__ == '__main__':
  a = [3, 2]
  b = [1, 4]
  k = 2
  print(Solution().maxCombinations(a, b, k))  # [7, 6]

  a = [1, 4, 2, 3]
  b = [2, 5, 1, 6]
  k = 3
  print(Solution().maxCombinations(a, b, k))  # [10, 9, 9]