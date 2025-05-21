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
from queue import Queue

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Maximum width of a binary tree
# Time Complexity: O(N)
# Space Complexity: O(N)
def widthOfBinaryTree(root) -> int:
  if root is None:
    return 0
  
  ans = 0
  q = Queue()
  q.put((root, 0))

  while q:
    size = q.qsize()
    mmin = q.queue[0][1]
    first, last = None, None
    
    for i in range(size):
      curr_id = q.queue[0][1] - mmin
      node = q.queue[i][0]
      
      if i == 0:
        first = curr_id

      if i == size - 1:
        last = curr_id

      if node.left:
        q.put((node.left, curr_id * 2 + 1))
      if node.right:
        q.put((node.right, curr_id * 2 + 2))

    ans = max(ans, last - first + 1)
  
  return ans

if __name__ == "__main__":
  root = TreeNode(3)
  root.left = TreeNode(5)
  root.right = TreeNode(1)
  root.left.left = TreeNode(6)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(0)
  root.right.right = TreeNode(8)
  root.left.right.left = TreeNode(7)
  root.left.right.right = TreeNode(4)

  result = widthOfBinaryTree(root)
  print("The maximum width of the binary tree: ", result)

 