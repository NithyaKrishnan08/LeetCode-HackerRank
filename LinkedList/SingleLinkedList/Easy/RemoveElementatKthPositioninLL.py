# Remove Element at Kth Position in Linked List
# Difficulty: Easy

'''
Given a Linked List and an integer k, remove the element at the kth position of the linked list.

Example
List: 1→3→4→7
k: 2
Result: 1→4→7
'''

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next
		  
class Solution:
  def removekthElement(self, head: ListNode, k: int) -> ListNode:
    if head is None:
      return None
    
    count = 1
    temp = head
    prev = None

    while temp and count < k:
      prev = temp
      temp = temp.next
      count += 1
      if count == k:
        if prev:
          prev.next = temp.next
        else:
          head = temp.next
        break

    return head

if __name__ == "__main__":
  # Create a linked list 1 -> 3 -> 4 -> 7
  head = ListNode(1)
  head.next = ListNode(3)
  head.next.next = ListNode(4)
  head.next.next.next = ListNode(7)

  k = 2

  solution = Solution()
  new_head = solution.removekthElement(head, k)

  # Print the modified linked list
  temp = new_head
  while temp:
    print(temp.data, end=" -> " if temp.next else "")
    temp = temp.next
  print()


		