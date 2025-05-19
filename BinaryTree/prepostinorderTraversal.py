class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Pre, Post and Inorder Iterative Traversal of a binary tree using 1 stack
# Time Complexity: O(3N)
# Space Complexity: O(4N)
def preInPostorderTraversal(root):
  pre_order, in_order, post_order = [], [], []
  
  if root is None:
    return []
  
  stack = [(root, 1)]

  while stack:
    node, state = stack.pop()

    if state == 1:
      pre_order.append(node.val)
      state = 2
      stack.append((node, state))
      if node.left:
        stack.append((node.left, 1))
    elif state == 2:
      in_order.append(node.val)
      state = 3
      stack.append((node, state))
      if node.right:
        stack.append((node.right, 1))
    else:
      post_order.append(node.val)
  
  return pre_order, in_order, post_order

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  result = preInPostorderTraversal(root)
  pre_order, in_order, post_order = result

  print("Pre-order traversal:", end=" ")
  print(pre_order)

  print("In-order traversal:", end=" ")
  print(in_order)

  print("Post-order traversal:", end=" ")
  print(post_order)

