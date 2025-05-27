'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

# This is Fibonaaci series
# Space Optimization
# Time Complexity: O(N)
# Space Complexity: O(1)

def climbStairs(n):
  m = n + 1
  prev2 = 0
  prev1 = 1
  if m <= 1:
    return m
  
  for i in range(2, m+1):
    curr = prev1 + prev2
    prev2 = prev1
    prev1 = curr
  return prev1

if __name__ == "__main__":
  n = 8
  result1 = climbStairs(n)
  print(f"Number of way to climb {n} staircase: {result1}")

