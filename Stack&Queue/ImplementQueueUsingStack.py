# Implement queue using stack
class Queue:
  def __init__(self):
    self.s1 = []
    self.s2 = []

  # TC: O(1)
  def enqueue(self, x: int) -> None:
    self.s1.append(x)

  # TC: O(N)
  def dequeue(self) -> int:
    if not self.s1:
      raise IndexError("Deque from empty queue")

    while self.s1:
      self.s2.append(self.s1.pop())

    front_element = self.s2.pop()

    while self.s2:
      self.s1.append(self.s2.pop())

    return front_element
  
  # TC: O(N)
  def front(self) -> int:
    if not self.s1:
      raise IndexError("Front from empty queue")
    
    while self.s1:
      self.s2.append(self.s1.pop())

    front_element = self.s2[-1]

    while self.s2:
      self.s1.append(self.s2.pop())

    return front_element
  
  # TC: O(1)
  def is_empty(self) -> bool:
    return len(self.s1) == 0
  
  # TC: O(1)
  def size(self) -> int:
    return len(self.s1)
  
if __name__ == "__main__":
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  print("Front element:", q.front())
  print("Dequeued:", q.dequeue())
  print("Front after dequeue:", q.front())
  print("Is queue empty?", q.is_empty())
  print("Queue size:", q.size())