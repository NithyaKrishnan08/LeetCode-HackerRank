'''
Find minimmum maximum in BST

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
  def findMinBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
      return None
    while root.left:
      root = root.left
    
    return root
  
  def findMaxBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
      return None
    while root.right:
      root = root.right
    
    return root
  
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
  min_val = solution.findMinBST(root)
  max_val = solution.findMaxBST(root)

  print(f"Minimum value in the BST: {min_val.val}")
  print(f"Maximum value in the BST: {max_val.val}")