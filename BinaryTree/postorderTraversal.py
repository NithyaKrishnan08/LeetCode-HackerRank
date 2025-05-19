class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Post-order Traversal of a binary tree
# Time Complexity: O(n)
# Space Complexity: O(h) - h is the height of the tree
def postOrderTraversal(treeNode, arr):
  if treeNode is None:
    return
  
  postOrderTraversal(treeNode.left, arr)
  postOrderTraversal(treeNode.right, arr)
  arr.append(treeNode.val) 

def traverseTree(treeNode):
  arr = []
  postOrderTraversal(treeNode, arr)
  return arr

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  result = traverseTree(root)
  print(result)

  print("Postorder Traversal:", end=" ")
  for val in result:
    print(val, end=" ")
  print()

