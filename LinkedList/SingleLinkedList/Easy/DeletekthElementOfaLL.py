# Delete the kth element of a Linked List
# Difficulty: Easy

'''
Problem Statement: Given a linked list, delete the kth element of the linked list and print the updated linked list.

Note: K will always be between 1 and N, where N is the length of the LL.

Example 1:
Input Format: 12->5->8->7, k=3

Result: 12->5->7

Explanation: Again, the third element of the list is 8. After removing the third node, the list has 5 pointing to 7, as shown in the result.

'''
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def deleteKthElement(self, head: ListNode, k: int) -> ListNode:
    if head is None:
      return None
    
    if k == 1:
      return head.next
    
    temp = head
    count = 1

    while temp and count < k - 1:
      temp = temp.next
      count += 1

    if temp and temp.next:
      temp.next = temp.next.next
      
    return head
  
if __name__ == "__main__":
  # Create a linked list: 12 -> 5 -> 8 -> 7
  head = ListNode(12)
  head.next = ListNode(5)
  head.next.next = ListNode(8)
  head.next.next.next = ListNode(7)

  k = 3

  solution = Solution()
  updated_head = solution.deleteKthElement(head, k)

  # Print the updated linked list
  temp = updated_head
  while temp:
    print(temp.val, end=" -> " if temp.next else "")
    temp = temp.next