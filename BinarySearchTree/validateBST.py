'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''
#  Kth smallest Element in a BST
from typing import List, Optional

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    return self.isValidBSTHelper(root, float('-inf'), float('inf'))
  
  def isValidBSTHelper(self, root, min_val, max_val):
    if root is None:
      return True
    if root.val <= min_val or root.val >= max_val:
      return False
    return (self.isValidBSTHelper(root.left, min_val, root.val) and (self.isValidBSTHelper(root.right, root.val, max_val)))
  
def printInorder(root):
  if not root:
      return
  printInorder(root.left)
  print(root.val, end=" ")
  printInorder(root.right)


if __name__ == "__main__":
  root = TreeNode(2)
  root.left = TreeNode(1)
  root.right = TreeNode(3)
  
  print("Binary Search Tree: ")
  printInorder(root)
  print()
  
  solution = Solution()
  result = solution.isValidBST(root)
  if result:
    print("The tree is a valid BST")
  else:
    print("The tree is not a valid BST")
