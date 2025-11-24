# Implement stack using Linked Lists

class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

class Queue:
  def __init__(self):
    self.start = None
    self.end = None
    self.size = 0

  # TC: O(1)
  # SC: O(size) 
  def push(self, x: int) -> None:
    temp = Node(x)
    if self.start == None:
      self.start = temp
      self.end = temp
    else:
      self.end.next = temp
    self.size += 1

  # TC: O(1)
  # SC: O(size)
  def pop(self) -> int:
    if self.start == None:
      print("Queue is empty")

    temp = self.start
    self.start = self.start.next
    popped_value = temp.val
    del temp
    
    self.size -= 1
    return popped_value
  
  # TC: O(1)
  # SC: O(size)
  def Top(self) -> int:
    if self.start == None:
      print("Queue is empty")
    return self.start.val
  
  # TC: O(1)
  # SC: O(size)
  def Size(self) -> int:
    return self.size
  
if __name__ == "__main__":
  q = Queue()
  q.push(6)
  q.push(3)
  q.push(7)
  print("Top of queue before deleting any element", q.Top())
  print("Size of queue before deleting any element", q.Size())
  print("The deleted element: ", q.pop())
  print("Size of queue after deleting an element", q.Size())
  print("Top of queue after deleting an element", q.Top())