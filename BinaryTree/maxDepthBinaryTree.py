'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

'''
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Maximum Depth of a binary tree - using level order traversal
# Time Complexity: O(N)
#  Space Complexity: O(N)
def maxDepth1(root) -> int:
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

    max_depth = len(ans)
  
  return max_depth

# Maximum Depth of a binary tree - using recursion method
# Time Complexity: O(N)
# Space Cmoplexity: O(N)
def maxDepth2(root) -> int:
  if root is None:
    return 0
  
  leftDepth = maxDepth2(root.left)
  rightDepth = maxDepth2(root.right)

  return 1 + max(leftDepth, rightDepth)

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.left.right.right = TreeNode(6)
  root.left.right.right.right = TreeNode(7)

  print("Level order traversal: ")
  result1 = maxDepth1(root)
  print("The maximum depth of the binary tree: ", result1)

  print("Recursion method: ")
  result2 = maxDepth2(root)
  print("The maximum depth of the binary tree: ", result2)
 