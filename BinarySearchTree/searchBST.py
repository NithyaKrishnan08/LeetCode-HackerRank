'''
Given a Binary Search Tree and a key value return the node in the BST having data equal to ‘key’ otherwise return nullptr.

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
  def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    while root is not None and root.val != target:
      if target < root.val:
        root = root.left
      else:
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
  target = 4
  result = solution.searchBST(root, target)

  if result is not None:
    print(f"Value {target} is found in the BST.")
  else:
    print(f"Value {target} is not found in the BST.")