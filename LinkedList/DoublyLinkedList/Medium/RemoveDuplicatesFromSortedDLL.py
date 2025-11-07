# Remove duplicates from a sorted doubly linked list
# Difficulty: Medium

'''
Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.

Example 1:

Input:
n = 6
1<->1<->1<->2<->3<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of node with value 1 is 
retained, rest nodes with value = 1 are deleted.
Example 2:

Input:
n = 7
1<->2<->2<->3<->3<->4<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of nodes with values 2,3 and 4 are 
retained, rest repeating nodes are deleted.
'''

class Node:
  def __init__(self, data, next=None, prev=None,):
    self.data = data
    self.next = next
    self.prev = prev

def removeDuplicatesDLL(head):
  if not head:
    return head
  
  temp = head
  while temp and temp.next:
    if temp.data == temp.next.data:
      next_next = temp.next.next
      temp.next = next_next
      if next_next:
        next_next.prev = temp
    else:
      temp = temp.next

  return head

if __name__ == "__main__":
  # Example usage:
  head = Node(1)
  head.next = Node(1, prev=head)
  head.next.next = Node(1, prev=head.next)
  head.next.next.next = Node(2, prev=head.next.next)
  head.next.next.next.next = Node(3, prev=head.next.next.next)
  head.next.next.next.next.next = Node(4, prev=head.next.next.next.next)

  new_head = removeDuplicatesDLL(head)

  # Print the modified list
  temp = new_head
  while temp:
    print(temp.data, end=" <-> " if temp.next else "")
    temp = temp.next