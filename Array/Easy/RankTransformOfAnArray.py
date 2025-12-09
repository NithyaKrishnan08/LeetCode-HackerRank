# Rank Transform of an Array
# https://leetcode.com/problems/rank-transform-of-an-array/description/
# Leetcode: 1331
# Difficulty: Easy

'''
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
 

Constraints:

0 <= arr.length <= 105
-109 <= arr[i] <= 109
'''
from typing import List
import heapq

class Solution:
  def arrayRankTransformSort(self, arr: List[int]) -> List[int]:
    sorted_unique = sorted(set(arr))
    rank_map = {value: index + 1 for index, value in enumerate(sorted_unique)}
    return [rank_map[num] for num in arr]
  
  def arrayRankTransformHeap(self, arr: List[int]) -> List[int]:
    if not arr:
      return []
    
    heap = [(val, idx) for idx, val in enumerate(arr)]
    heapq.heapify(heap)

    result = [0] * len(arr)
    rank = 1
    prev_val = None

    while heap:
      val, idx = heapq.heappop(heap)
      if val != prev_val:
        prev_val = val
        result[idx] = rank
        rank += 1
      else:
        result[idx] = rank - 1

    return result
  
if __name__ == "__main__":
  solution = Solution()

  arr = [40,10,20,30]
  result = solution.arrayRankTransformSort(arr)
  print(f"The rank transform of the array {arr} using sorting is: {result}")

  arr = [100,100,100]
  result = solution.arrayRankTransformSort(arr)
  print(f"The rank transform of the array {arr} using sorting is: {result}")

  arr = [37,12,28,9,100,56,80,5,12]
  result = solution.arrayRankTransformSort(arr)
  print(f"The rank transform of the array {arr} using sorting is: {result}")

  arr = [40,10,20,30]
  result = solution.arrayRankTransformHeap(arr)
  print(f"The rank transform of the array {arr} using heap is: {result}")

  arr = [100,100,100]
  result = solution.arrayRankTransformHeap(arr)
  print(f"The rank transform of the array {arr} using heap is: {result}")

  arr = [37,12,28,9,100,56,80,5,12]
  result = solution.arrayRankTransformHeap(arr)
  print(f"The rank transform of the array {arr} using heap is: {result}")