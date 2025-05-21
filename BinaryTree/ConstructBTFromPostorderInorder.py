'''
Problem Statement: Given the Postorder and Inorder traversal of a Binary Tree, construct the Unique Binary Tree represented by them.

'''
from typing import List, Optional

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Time Complexity: O(N)
#  Space Complexity: O(N + log(N))
class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    
    if len(inorder) != len(postorder):
      return None
    
    inMap = {val: index for index, val in enumerate(inorder)}

    root = self._buildTree(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, inMap)

    return root
  
  def _buildTree(self, inorder, inStart, inEnd, postorder, postStart, postEnd, inMap):
    
    if postStart > postEnd or inStart > inEnd:
      return None
    
    root = TreeNode(postorder[postEnd])
    inRoot = inMap[root.val]
    numsLeft = inRoot - inStart

    root.left = self._buildTree(inorder, inStart, inRoot - 1, postorder, postStart, postStart + numsLeft - 1, inMap)

    root.right = self._buildTree(inorder, inRoot + 1, inEnd, postorder, postStart + numsLeft, postEnd - 1, inMap)

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
  inorder = [40, 20, 50, 10, 60, 30]
  postorder = [40, 50, 20, 60, 30, 10]
  
  print("Inorder List: ", end="")
  printList(inorder)
  
  print("Postorder List: ", end="")
  printList(postorder)
  
  sol = Solution()

  root = sol.buildTree(inorder, postorder)
  
  print("Inorder of Unique Binary Tree Created:")
  printInorder(root)
  print()