# Check if an array represents a min heap

'''
Problem Statement: Given an array of integers nums. Check whether the array represents a binary min-heap or not. Return true if it does, otherwise return false.
A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.

Examples
Input: nums = [10, 20, 30, 21, 23]
Output: true
Explanation: Each node has a lower or equal value than its children.

Input: nums = [10, 20, 30, 25, 15]
Output: false
Explanation: The node with value 20 has a child with value 15, thus it is not a min-heap.
'''

class Solution:
  def isMinHeap(self, nums):
    n = len(nums)

    # Check for each internal node if it is less than or equal to its children
    for i in range(n // 2):
      left = 2 * i + 1
      right = 2 * i + 2

      if left < n and nums[i] > nums[left]:
        return False

      if right < n and nums[i] > nums[right]:
        return False
      
    return True
  

if __name__ == "__main__":
  sol = Solution()

  # Test case 1
  nums1 = [10, 20, 30, 21, 23]
  print(sol.isMinHeap(nums1))  # Expected output: True

  # Test case 2
  nums2 = [10, 20, 30, 25, 15]
  print(sol.isMinHeap(nums2))  # Expected output: False
