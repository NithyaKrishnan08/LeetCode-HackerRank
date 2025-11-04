# Sort a LL of 0's 1's and 2's by changing links

'''
Given a head of linked list containing nodes with values 0, 1, and 2 only, rearrange the list so that all 0s appear first, followed by all 1s, and then all 2s at the end, while maintaining the relative order within each group.
'''

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def sortLL012(self, head: ListNode) -> ListNode:
    if not head or not head:
      return head
    
    zeroD = ListNode(0)
    oneD = ListNode(0)
    twoD = ListNode(0)

    zero = zeroD
    one = oneD
    two = twoD

    curr = head
    while curr:
      if curr.val == 0:
        zero.next = curr
        zero = zero.next
      elif curr.val == 1:
        one.next = curr
        one = one.next
      else:
        two.next = curr
        two = two.next
      curr = curr.next

    # Combine three lists
    zero.next = oneD.next if oneD.next else twoD.next
    one.next = twoD.next
    two.next = None

    head = zeroD.next

    return head
  

if __name__ == '__main__':
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(2)
  head.next.next.next = ListNode(1)
  head.next.next.next.next = ListNode(2)
  head.next.next.next.next.next = ListNode(0)
  head.next.next.next.next.next.next = ListNode(2)
  head.next.next.next.next.next.next.next = ListNode(2)

  sol = Solution()

  new_head = sol.sortLL012(head)

  # Print the modified linked list
  temp = new_head
  while temp:
    print(temp.val, end=" -> " if temp.next else "")
    temp = temp.next
  print()
