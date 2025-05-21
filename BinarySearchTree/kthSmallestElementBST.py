'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 
Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
'''
#  Kth smallest Element in a BST
from typing import List, Optional

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Time Complexity: O(log2N)
# Space Complexity: O(1)
class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    self.k = k
    self.result = None
    self.inorderTraversal(root)
    return self.result
  
  def inorderTraversal(self, node):
    if not node or self.result is not None:
      return
    self.inorderTraversal(node.left)
    self.k -= 1
    if self.k == 0:
      self.result = node.val
      return
    self.inorderTraversal(node.right)
  
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
  k = 3
  result = solution.kthSmallest(root, k)
  print(f"{k}th smallest element: {result}")
