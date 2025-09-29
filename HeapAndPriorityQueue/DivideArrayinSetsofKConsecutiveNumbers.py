# Divide Array in Sets of K Consecutive Numbers
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
# Leetcode: 1296

# Same as question: Hand of Straights
# https://leetcode.com/problems/hand-of-straights/description/
# Leetcode: 846

'''
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 109
'''
from typing import List
from collections import Counter
import heapq

class Solution:
  def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    if len(nums) % k:
        return False

    count = Counter(nums)
    minHeap = list(count.keys())
    heapq.heapify(minHeap)

    while minHeap:
      first = minHeap[0]

      for num in range(first, first + k):
        if num not in count:
          return False

        count[num] -= 1
        if count[num] == 0:
          if num != minHeap[0]:
            return False
          heapq.heappop(minHeap)

    return True
  
if __name__ == "__main__":
  solution = Solution()
  tests = [
    ([1,2,3,3,4,4,5,6], 4, True),
    ([3,2,1,2,3,4,3,4,5,9,10,11], 3, True),
    ([1,2,3,4], 3, False),
  ]

  for nums, k, ans in tests:
    res = solution.isPossibleDivide(nums, k)
    print(res == ans, res)



        