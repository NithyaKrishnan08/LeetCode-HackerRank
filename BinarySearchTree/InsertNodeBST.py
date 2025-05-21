'''
Problem Statement: Insert a given node into a Binary Search Tree (BST)

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
  def insertBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
      return TreeNode(val)
    
    current_node = root
    
    while True:
      if current_node.val <= val:
        if current_node.right is not None:
          current_node = current_node.right
        else:
          current_node.right = TreeNode(val)
          break
      else:
        if current_node.left is not None:
          current_node = current_node.left
        else:
          current_node.left = TreeNode(val)
          break
    
    return root
  
def printInorder(root):
  if not root:
      return
  printInorder(root.left)
  print(root.val, end=" ")
  printInorder(root.right)


if __name__ == "__main__":
  root = TreeNode(6)
  root.left = TreeNode(3)
  root.right = TreeNode(8)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(4)
  root.right.left = TreeNode(7)
  
  print("Binary Search Tree: ")
  printInorder(root)
  print()
  
  solution = Solution()
  key = 5
  result_root = solution.insertBST(root, key)
  print("Binary Search Tree after inserting node: ")
  printInorder(result_root)
  print()