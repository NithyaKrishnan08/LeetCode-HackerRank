'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
'''
from typing import Optional, List
from queue import Queue

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
  def serialize(self, root: Optional[TreeNode]) -> str:
    if root is None:
      return ""
    
    serialize_str = ""
    q = Queue()
    q.put(root)

    while not q.empty():
      curr_node = q.get()

      if not curr_node:
        serialize_str += "null,"
      else:
        serialize_str += str(curr_node.val) + ","
        q.put(curr_node.left)
        q.put(curr_node.right)
    
    return serialize_str[:-1]
  
  def deserialize(self, data) -> str:
    if not data:
      return None
    
    q = Queue()
    node_values = data.split(",")
    root_val = int(node_values.pop(0))
    root = TreeNode(root_val)
    q.put(root)

    while not q.empty():
      curr_node = q.get()
      
      left_val = node_values.pop(0)
      if left_val != "null":
        left_node = TreeNode(int(left_val))
        curr_node.left = left_node
        q.put(left_node)

      right_val = node_values.pop(0)
      if right_val != "null":
        right_node = TreeNode(int(right_val))
        curr_node.right = right_node
        q.put(right_node)

    return root
  
def inorderTraversal(root):
  if not root:
    return
  
  inorderTraversal(root.left)
  print(root.val, end=" ")
  inorderTraversal(root.right)

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.right.left = TreeNode(4)
  root.right.right = TreeNode(5)

  solution = Solution()
  print("Original Tree: ", end="")
  inorderTraversal(root)
  print()

  serialized_tree = solution.serialize(root)
  print("Serialized tree: ", serialized_tree)

  deserialized_tree = solution.deserialize(serialized_tree)
  print("De-Serialized tree: ", deserialized_tree)
  inorderTraversal(deserialized_tree)
  print()
    