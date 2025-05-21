'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
'''

from typing import List, Optional

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Binary tree maximum path sum
# Time Complexity: O(N)
# Space Cmoplexity: O(1)
class Solution:
  def findMaxPathSum(self, root, maximum):
    if root is None:
      return 0
    
    leftMaxpath = max(0, self.findMaxPathSum(root.left, maximum))
    rightMaxpath = max(0, self.findMaxPathSum(root.right, maximum))

    maximum[0] = max(maximum[0], leftMaxpath + rightMaxpath + root.val)
    return max(leftMaxpath, rightMaxpath) + root.val

  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    maximum = [float('-inf')]
    self.findMaxPathSum(root, maximum)

    return maximum[0]

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.left.right.right = TreeNode(6)
  root.left.right.right.right = TreeNode(7)

  solution = Solution()
  maxPathSum = solution.maxPathSum(root)
  print("Maximum path sum of the binary tree: ", maxPathSum)
 