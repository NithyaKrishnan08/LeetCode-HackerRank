'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''
from typing import List, Optional

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Time Complexity: O(N)
#  Space Complexity: O(N)
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if len(inorder) != len(preorder):
      return None
    
    inMap = {val: index for index, val in enumerate(inorder)}

    root = self._buildTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inMap)

    return root
  
  def _buildTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
    
    if preStart > preEnd or inStart > inEnd:
      return None
    
    root = TreeNode(preorder[preStart])
    inRoot = inMap[root.val]
    numsLeft = inRoot - inStart

    root.left = self._buildTree(preorder, preStart + 1, preStart + numsLeft, inorder, inStart, inRoot - 1, inMap)

    root.right = self._buildTree(preorder, preStart + numsLeft + 1, preEnd, inorder, inRoot + 1, inEnd, inMap)

    return root
  
def printInorder(root):
  if not root:
      return
  printInorder(root.left)
  print(root.val, end=" ")
  printInorder(root.right)

def printList(lst):
  for val in lst:
    print(val, end=" ")
  print()

if __name__ == "__main__":
  inorder = [9, 3, 15, 20, 7]
  preorder = [3, 9, 20, 15, 7]
  
  print("Inorder List: ", end="")
  printList(inorder)
  
  print("Preorder List: ", end="")
  printList(preorder)
  
  sol = Solution()

  root = sol.buildTree(preorder, inorder)
  
  print("Inorder of Unique Binary Tree Created:")
  printInorder(root)
  print()