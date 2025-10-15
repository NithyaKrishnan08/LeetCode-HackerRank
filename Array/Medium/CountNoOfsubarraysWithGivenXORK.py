# Count the number of subarrays with given xor K

'''
Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.

Example 1:
Input Format: A = [4, 2, 2, 6, 4] , k = 6
Result: 4
Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]

Example 2:
Input Format: A = [5, 6, 7, 8, 9], k = 5
Result: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]
'''
from typing import List

class Solution:
  def subarrayXor(self, A: List[int], k: int) -> int:
    xor_count = {}
    prefix_xor = 0
    count = 0

    for num in A:
      prefix_xor ^= num

      if prefix_xor == k:
        count += 1

      required_xor = prefix_xor ^ k
      if required_xor in xor_count:
        count += xor_count[required_xor]

      xor_count[prefix_xor] = xor_count.get(prefix_xor, 0) + 1

    return count
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.subarrayXor([4, 2, 2, 6, 4], 6))  # 4
  print(sol.subarrayXor([5, 6, 7, 8, 9], 5))  # 2