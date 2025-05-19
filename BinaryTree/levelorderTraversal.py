from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Level-order Traversal of a binary tree
# Time Complexity: O(n)
# Space Complexity: O(n)
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

def printList(lst):
  for num in lst:
    print(num, end=" ")
  print()

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)

  result = levelOrderTraversal(root)
  print("Level Order Traversal of Tree:")
  for level in result:
    printList(level)

