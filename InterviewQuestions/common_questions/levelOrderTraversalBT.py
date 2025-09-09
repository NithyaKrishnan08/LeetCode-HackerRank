from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def levelOrderTraversal(root):
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