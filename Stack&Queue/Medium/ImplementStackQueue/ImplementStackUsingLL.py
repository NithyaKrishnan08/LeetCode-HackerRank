# Implement stack using Linked Lists
class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0

  # TC: O(1)
  # SC: O(size)
  def push(self, x: int) -> None:
    temp = Node(x)
    temp.next = self.top
    self.top = temp
    self.size += 1

  # TC: O(1)
  # SC: O(size)
  def pop(self) -> int:
    if self.top is None:
      raise IndexError("Pop from empty stack")
    
    temp = self.top
    self.top = self.top.next
    popped_val = temp.val
    del temp
    self.size -= 1
    return popped_val
  
  # TC: O(1)
  # SC: O(size)
  def Top(self) -> int:
    if self.top is None:
      raise IndexError("Pop from empty stack")
    return self.top.val
  
  # TC: O(1)
  # SC: O(size)
  def Size(self) -> int:
    return self.size
  
if __name__ == "__main__":
  s = Stack()
  s.push(6)
  s.push(3)
  s.push(7)
  print("Top of stack before deleting any element", s.Top())
  print("Size of stack before deleting any element", s.Size())
  print("The deleted element: ", s.pop())
  print("Size of stack after deleting an element", s.Size())
  print("Top of stack after deleting an element", s.Top())