# Connect N Ropes With Minimum Cost

'''
Problem statement
Given an array of integers A representing the length of ropes.You need to connect these ropes into one rope. The cost of connecting two ropes is equal to the sum of their lengths.Find and return the minimum cost to connect these ropes into one rope.
Given A = [4, 3, 2, 6] n = 4.
Output=29
1) If we first connect ropes of lengths 2 and 3, we will be left with three ropes of lengths 4, 6, and 5.
2) Now, if we connect ropes of lengths 4 and 5, we will be left with two ropes of lengths 6 and 9.
3) Finally, we connect the remaining two ropes, and all the ropes are now connected.
The total cost of connecting all the ropes in this way is 5 + 9 + 15 = 29, which is the optimised cost.
Now there are other ways to connect ropes. For example, if we connect 4 and 6 first (we get three ropes of lengths 3, 2, and 10), then connect 10 and 3 (we get two ropes of lengths 13 and 2). Finally, we connect 13 and 2. The total cost in this way is 10 + 13 + 15 = 38, which is not the optimal cost.
'''
import heapq

class Solution:
  def minCost(self, A):
    heapq.heapify(A)
    total_cost = 0

    while len(A) > 1:
      first_min = heapq.heappop(A)
      second_min = heapq.heappop(A)
      cost = first_min + second_min
      total_cost += cost
      heapq.heappush(A, cost)

    return total_cost
  
if __name__ == "__main__":
  solution = Solution()
  A = [4, 3, 2, 6]
  print(f"Input: {A}")
  result = solution.minCost(A)
  print(f"Output: {result}")