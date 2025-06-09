# Implement stack using queue
from collections import deque

class Stack:
  def __init__(self):
    self.q1 = deque()
    self.q2 = deque()

  # TC: O(N)
  # SC: O(N)
  def push(self, x: int) -> None:
    self.q2.append(x)
    while self.q1:
      self.q2.append(self.q1.popleft())

    self.q1, self.q2 = self.q2, self.q1

  # TC: O(1)
  # SC: O(N)
  def pop(self) -> int:
    if not self.q1:
      raise IndexError("Pop from empty stack")
    return self.q1.popleft()
  
  # TC: O(1)
  # SC: O(N)
  def top(self) -> int:
    if not self.q1:
      raise IndexError("Pop from empty stack")
    return self.q1[0]
  
  # TC: O(1)
  # SC: O(N)
  def size(self) -> int:
    return len(self.q1)
  
if __name__ == "__main__":
  s = Stack()
  s.push(10)
  s.push(20)
  s.push(30)
  print("Top element:", s.top())
  print("Popped element:", s.pop())
  print("Current top:", s.top())
  print("Current size:", s.size()) 