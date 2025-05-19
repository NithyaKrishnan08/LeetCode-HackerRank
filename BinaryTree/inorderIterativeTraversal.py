class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Inorder Iterative Traversal of a binary tree
# Time Complexity: O(n)
# Space Complexity: O(n)
def inOrderIterativeTraversal(root):
  inorder = []
  if root is None:
    return inorder
  
  st = []
  node = root

  while node is not None or st:
    while node is not None:
      st.append(node)
      node = node.left
    
    node = st.pop()
    inorder.append(node.val)

    node = node.right
  
  return inorder

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  result = inOrderIterativeTraversal(root)

  print("Inorder Iterative Traversal:", end=" ")
  print(result)

