'''
Problem Statement: Given a Binary Search Tree and a key, return the ceiling of the given key in the Binary Search Tree.

Ceiling of a value refers to the value of the smallest node in the Binary Search Tree that is greater than or equal to the given key.
If the ceiling node does not exist, return nullptr.

'''
from typing import List, Optional

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Time Complexity: O(log2N)
# Space Complexity: O(1)
class Solution:
  def ceilBST(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    ceil = float('-inf')
    while root is not None:
      if root.val == key:
        ceil = root.val
        return ceil
      
      if key > root.val:
        root = root.right
      else:
        ceil = root.val
        root = root.left
    
    return ceil
  
def printInorder(root):
  if not root:
      return
  printInorder(root.left)
  print(root.val, end=" ")
  printInorder(root.right)


if __name__ == "__main__":
  root = TreeNode(5)
  root.left = TreeNode(3)
  root.right = TreeNode(8)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(4)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(10)
  
  print("Binary Search Tree: ")
  printInorder(root)
  print()
  
  solution = Solution()
  key = 7
  result = solution.ceilBST(root, key)
  print(f"Ceil of {key} in the BST: {result}")