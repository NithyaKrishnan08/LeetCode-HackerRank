'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''
#  Subtree of another tree
from typing import List, Optional

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
      return True
    if not p or not q or p.val != q.val:
      return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root:
      return False
    if self.isSameTree(root, subRoot):
      return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
  
if __name__ == "__main__":
  root = TreeNode(3)
  root.left = TreeNode(4)
  root.right = TreeNode(5)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(2)
  root.left.right.left = TreeNode(0)

  subRoot = TreeNode(4)
  subRoot.left = TreeNode(1)
  subRoot.right = TreeNode(2)

  solution = Solution()
  result = solution.isSubtree(root, subRoot)
  if result:
    print("SubRoot is a subtree of the root")
  else:
    print("SubRoot is not a subtree of the root")