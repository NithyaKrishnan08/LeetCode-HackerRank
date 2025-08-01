# Jump Game II

'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
'''
from typing import List

class Solution:

  # Brute Force Solution
  # TC: O(2^N)
  # SC: O(N)
  def jump1(self, nums: List[int]) -> int:
    n = len(nums)

    def jumps_recursive(index, jumps):
      if index >= n - 1:
        return jumps

      minimum_jumps = float('inf')

      for i in range(1, nums[index] + 1):
        minimum_jumps = min(minimum_jumps, jumps_recursive(index + i, jumps + 1))

      return minimum_jumps

    return jumps_recursive(0, 0)
  
  # Optimal Solution - Greedy Algorithm
  # TC: O(N)
  # SC: O(1)
  def jump(self, nums: List[int]) -> int:
    n = len(nums)
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
      farthest = max(farthest, nums[i] + i)
      if i == current_end:
        jumps += 1
        current_end = farthest

    return jumps
  
if __name__ == "__main__":
  solution = Solution()
  nums = [2,3,1,1,4]
  result = solution.jump(nums)
  print(result)