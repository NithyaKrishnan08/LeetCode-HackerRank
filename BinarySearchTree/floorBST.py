'''
Problem Statement: Given a Binary Search Tree and a key, return the floor of the given key in the Binary Search Tree.

Floor of a value refers to the value of the largest node in the Binary Search Tree that is smaller than or equal to the given key.
If the floor node does not exist, return nullptr.

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
  def floorBST(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    floor = float('inf')
    while root is not None:
      if root.val == key:
        floor = root.val
        return floor
      
      if key > root.val:
        floor = root.val
        root = root.right
      else:
        root = root.left
    
    return floor
  
def printInorder(root):
  if not root:
      return
  printInorder(root.left)
  print(root.val, end=" ")
  printInorder(root.right)


if __name__ == "__main__":
  root = TreeNode(10)
  root.left = TreeNode(5)
  root.right = TreeNode(13)
  root.left.left = TreeNode(3)
  root.left.left.left = TreeNode(2)
  root.left.left.right = TreeNode(4)
  root.left.right = TreeNode(6)
  root.left.right.right = TreeNode(9)
  root.right.left = TreeNode(11)
  root.right.right = TreeNode(14)
  
  print("Binary Search Tree: ")
  printInorder(root)
  print()
  
  solution = Solution()
  key = 8
  result = solution.floorBST(root, key)
  print(f"Floor of {key} in the BST: {result}")