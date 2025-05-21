'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''

from collections import deque
from typing import List, Optional

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Same Tree or not
# Time Complexity: O(2N)
# Space Complexity: O(2N)
def levelOrderTraversal(root) -> List[int]:
  ans = []
  if root is None:
    return ans
  
  q = deque()
  q.append(root)

  while q:
    size = len(q)
    level = []
    
    for _ in range(size):
      node = q.popleft()
      level.append(node.val)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)

    ans.append(level)
  
  return ans

def isSameTree1(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
  list1 = levelOrderTraversal(p)
  list2 = levelOrderTraversal(q)

  if list1 == list2:
    return True
  
  return False

# Maximum Depth of a binary tree - using recursion method
# Time Complexity: O(N)
# Space Cmoplexity: O(N)
def isSameTree2(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
  if p is None and q is None:
    return True
  if p is None or q is None:
    return False

  return (p.val == q.val) and isSameTree2(p.left, q.left) and isSameTree2(p.right, q.right)

if __name__ == "__main__":
  root1 = TreeNode(1)
  root1.left = TreeNode(2)
  root1.right = TreeNode(3)
  root1.left.left = TreeNode(4)

  root2 = TreeNode(1)
  root2.left = TreeNode(2)
  root2.right = TreeNode(3)
  root2.left.left = TreeNode(4)

  print("Level order traversal: ")
  result1 = isSameTree1(root1, root2)
  if result1:
    print("The two binary trees are the same.")
  else:
    print("the two binary trees are not the same.")

  print("Recursion method: ")
  result2 = isSameTree2(root1, root2)
  if result2:
    print("The two binary trees are the same.")
  else:
    print("the two binary trees are not the same.")
 