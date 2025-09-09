'''
Problem Statement: Given a Binary Tree, determine whether the given tree is symmetric or not. A Binary Tree would be Symmetric, when its mirror image is exactly the same as the original tree. If we were to draw a vertical line through the centre of the tree, the nodes on the left and right side would be mirror images of each other.
'''

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Symmetric Binary Tree
# Time Complexity: O(n)
# Space Complexity: O(n)
def isSymmetricUtil(left_node, right_node):
  if left_node is None or right_node is None:
    return True
  
  if left_node is None or right_node is None:
    return False
  
  if (left_node.val != right_node.val):
    return False
  
  return isSymmetricUtil(left_node.left, right_node.right) and isSymmetricUtil(left_node.right, right_node.left)

def isSymmetric(root):
  if root is None:
    return True
  
  return isSymmetricUtil(root.left, root.right)

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(4)
  root.right = TreeNode(4)
  root.left.left = TreeNode(1)
  root.right.right = TreeNode(1)

  result = isSymmetric(root)
  print(result)

