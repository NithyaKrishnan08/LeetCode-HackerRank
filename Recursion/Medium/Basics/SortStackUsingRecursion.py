# Sort a stack using recursion

'''
Given a stack of integers st[], Sort the stack in ascending order (smallest element at the bottom and largest at the top).

Example: 

Input: st[] = [1, 2, 3]
Output: [3, 2, 1]
Explanation: The stack is already sorted in ascending order.

2
 
Input: st[] = [41, 3, 32, 2, 11]
Output: [41, 32, 11, 3, 2]
Explanation: After sorting, the smallest element (2) is at the bottom and the largest element (41) is at the top.
'''

class Solution:
  def insertSorted(self, st, element):
    if not st or st[-1] <= element:
      st.append(element)
      return
    
    top = st.pop()
    self.insertSorted(st, element)

    st.append(top)

  def sortStack(self, st):
    if not st:
      return
    
    top = st.pop()
    self.sortStack(st)

    self.insertSorted(st, top)


if __name__ == "__main__":
  st = [41, 3, 32, 2, 11]
  solution = Solution()
  solution.sortStack(st)
  print(st)  # Output should be [41, 32, 11, 3, 2]
