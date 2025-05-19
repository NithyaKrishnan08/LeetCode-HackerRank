class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Inorder Traversal of a binary tree
# Time Complexity: O(n)
# Space Complexity: O(h) - h is the height of the tree
def inOrderTraversal(treeNode, arr):
  if treeNode is None:
    return
  
  inOrderTraversal(treeNode.left, arr)
  arr.append(treeNode.val)
  inOrderTraversal(treeNode.right, arr)

def traverseTree(treeNode):
  arr = []
  inOrderTraversal(treeNode, arr)
  return arr

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  result = traverseTree(root)
  print(result)

  print("Inorder Traversal:", end=" ")
  for val in result:
    print(val, end=" ")
  print()

