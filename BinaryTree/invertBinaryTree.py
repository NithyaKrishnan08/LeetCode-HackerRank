'''
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
'''

from typing import List, Optional

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Invert binary tree - using recursion method
# Time Complexity: O(N)
# Space Cmoplexity: O(N)
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
  if root is None:
    return root

  root.left, root.right = root.right, root.left

  invertTree(root.left)
  invertTree(root.right)

  return root

if __name__ == "__main__":
  root = TreeNode(4)
  root.left = TreeNode(2)
  root.right = TreeNode(7)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(9)


  print("Recursion method: ")
  result = invertTree(root)
  print(result)
 