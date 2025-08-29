# All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
# Leetcode Problem 863: All Nodes Distance K in Binary Tree

'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
'''
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    # Step 1: Build parent map
    parent_map = {}

    def dfs(node, parent = None):
      if not node:
        return
      parent_map[node] = parent
      dfs(node.left, node)
      dfs(node.right, node)

    dfs(root)

    # Step 2: BFS from target node
    queue = deque([(target, 0)])
    seen = {target}

    result = []
    while queue:
      node, dist = queue.popleft()

      if dist == k:
        result.append(node.val)

      elif dist < k:
        for neighbor in (node.left, node.right, parent_map[node]):
          if neighbor and neighbor not in seen:
            seen.add(neighbor)
            queue.append((neighbor, dist + 1))

    return result

if __name__ == "__main__":
  root = TreeNode(3)
  root.left = TreeNode(5)
  root.right = TreeNode(1)
  root.left.left = TreeNode(6)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(0)
  root.right.right = TreeNode(8)
  root.left.right.left = TreeNode(7)
  root.left.right.right = TreeNode(4)

  target = root.left  # Node with value 5
  k = 2

  s = Solution()
  print(s.distanceK(root, target, k))  # Output: [7,4,1]            