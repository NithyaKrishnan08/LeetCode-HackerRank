class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Preorder Traversal of a binary tree
# Time Complexity: O(n)
# Space Complexity: O(h) - h is the height of the tree
def preOrderTraversal(treeNode, arr):
  if treeNode is None:
    return
  
  arr.append(treeNode.val)

  preOrderTraversal(treeNode.left, arr)
  preOrderTraversal(treeNode.right, arr)


def traverseTree(treeNode):
  arr = []
  preOrderTraversal(treeNode, arr)
  return arr

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  result = traverseTree(root)
  print(result)

  print("Preorder Traversal:", end=" ")
  for val in result:
    print(val, end=" ")
  print()

