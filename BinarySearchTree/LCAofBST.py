'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
 
Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
'''
# LCA (Lowest Common Ancestor) in a BST
from typing import List, Optional

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Time Complexity: O(H) - H is the height of the BST
# Space Complexity: O(1)
class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None:
      return None
    cur_val = root.val
    if cur_val > p.val and cur_val > q.val:
      return self.lowestCommonAncestor(root.left, p, q)
    if cur_val < p.val and cur_val < q.val:
      return self.lowestCommonAncestor(root.right, p, q)
    
    return root
  
def printInorder(root):
  if not root:
    return
  printInorder(root.left)
  print(root.val, end=" ")
  printInorder(root.right)


if __name__ == "__main__":
  root = TreeNode(6)
  root.left = TreeNode(2)
  root.right = TreeNode(8)
  root.left.left = TreeNode(0)
  root.left.right = TreeNode(4)
  root.left.right.left = TreeNode(3)
  root.left.right.right = TreeNode(5)
  root.right.left = TreeNode(7)
  root.right.right = TreeNode(9)

  print("Binary Search Tree: ")
  printInorder(root)
  print()
  
  solution = Solution()
  p = root.left
  q = root.right

  result = solution.lowestCommonAncestor(root, p, q)
  if result:
    print(f"The LCA of {p.val} and {q.val} in BST: {result.val}")
