# K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
# Leetcode: 532

'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
 

Constraints:

1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107
'''
from typing import List
from collections import Counter

class Solution:
  # TC: O(n^2)
  # SC: O(1)
  def findPairsBrute(self, nums: List[int], k: int) -> int:
    n = len(nums)
    nums.sort()
    pairs = set()

    for i in range(n):
      for j in range(i + 1, n):
        diff = nums[j] - nums[i]
        if diff == k:
          pairs.add((nums[i], nums[j]))
          break
        elif diff > k:
          break
    
    return len(pairs)
  
  # Optimal approach
  # TC: O(n)
  # SC: O(n)
  def findPairs(self, nums: List[int], k: int) -> int:
    if k < 0:
      return 0
    
    count = 0
    freq = Counter(nums)

    if k == 0:
      for num in freq:
        if freq[num] > 1:
          count += 1
    else:
      for num in freq:
        if num + k in freq:
          count += 1

    return count
  
if __name__ == '__main__':
  solution = Solution()
  print(solution.findPairs([3,1,4,1,5], 2))
  print(solution.findPairs([1,2,3,4,5], 1))
  print(solution.findPairs([1,3,1,5,4], 0))
        