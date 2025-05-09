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

