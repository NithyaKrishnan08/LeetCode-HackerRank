class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Post Iterative Traversal of a binary tree using two stacks
# Time Complexity: O(n)
# Space Complexity: O(2n)
def postOrderIterative2stacksTraversal(root):
  postorder = []
  if root is None:
    return postorder
  
  st1, st2 = [], []
  st1.append(root)

  while st1:
    node = st1.pop()
    st2.append(node)

    if node.left is not None:
      st1.append(node.left)
    if node.right is not None:
      st1.append(node.right)

  while st2:
    node = st2.pop()
    postorder.append(node.val)
  
  return postorder

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  result = postOrderIterative2stacksTraversal(root)

  print("Inorder Iterative Traversal:", end=" ")
  print(result)

