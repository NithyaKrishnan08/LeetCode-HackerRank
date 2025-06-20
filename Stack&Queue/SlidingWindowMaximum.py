# Sliding Window Maximum

'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''
from typing import List
from collections import deque

class Solution:
  # Brute Force Solution
  # TC: O(n - k) * O(k)
  # SC: O(n - k)
  def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
    list = []
    n = len(nums)

    for i in range(n - k + 1):
      max_num = nums[i]
      for j in range(i, i + k):
        max_num = max(max_num, nums[j])
      list.append(max_num)

    return list
  
  # Optimal Solution
  # TC: O(2n)
  # SC: O(k) + O(n - k)
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    list = []
    dq = deque()
    n = len(nums)

    for i in range(n):
      if dq and dq[0] <= i - k:
        dq.popleft()

      while dq and nums[dq[-1]] <= nums[i]:
        dq.pop()

      dq.append(i)

      if i >= k - 1:
        list.append(nums[dq[0]])

    return list

if __name__ == "__main__":
  nums = [1,3,-1,-3,5,3,6,7]
  k = 3
  solution = Solution()
  result = solution.maxSlidingWindow(nums, k)
  print(result)