class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Post order Iterative Traversal of a binary tree using 1 stack
# Time Complexity: O(n)
# Space Complexity: O(2n)
def postOrderIterative1stack1Traversal(root):
  postorder = []
  if root is None:
    return postorder
  
  st = []
  last_visited = None
  current = root

  while current or st:
    if current:
      st.append(current)
      current = current.left
    else:
      peek_node = st[-1]
      if peek_node.right and last_visited != peek_node.right:
        current = peek_node.right
      else:
        postorder.append(peek_node.val)
        last_visited = st.pop()
  
  return postorder

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  result = postOrderIterative1stack1Traversal(root)

  print("Inorder Iterative Traversal:", end=" ")
  print(result)

