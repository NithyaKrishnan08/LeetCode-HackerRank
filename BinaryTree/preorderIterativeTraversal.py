class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Preorder Iterative Traversal of a binary tree
# Time Complexity: O(n)
# Space Complexity: O(n)
def preOrderIterativeTraversal(root):
  preorder = []
  if root is None:
    return preorder
  
  st = []
  st.append(root)

  while st:
    node = st.pop()
    preorder.append(node.val)

    if node.right:
      st.append(node.right)

    if node.left:
      st.append(node.left)
  
  return preorder


if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  result = preOrderIterativeTraversal(root)

  print("Preorder Iterative Traversal:", end=" ")
  for val in result:
    print(val, end=" ")
  print()

