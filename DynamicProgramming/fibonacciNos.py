# Recursive Fibonacci
# Time Complexity: O(N)
# Space Complexity : O(2N)
def fibonacci1(n, dp):
  if(n <= 1):
    return n
  if dp[n] != -1:
    return dp[n]
  dp[n] = fibonacci1(n-1, dp) + fibonacci1(n-2, dp)
  return dp[n]

#  Tabulation Fibonacci
def fibonacci2(n):
  prev2 = 0
  prev1 = 1
  if n <= 1:
    return n
  
  for i in range(2, n+1):
    curr = prev1 + prev2
    prev2 = prev1
    prev1 = curr
  return prev1

if __name__ == "__main__":
  n = 10
  dp = [-1] * (n + 1)
  result1 = fibonacci1(n, dp)
  print(f"The {n}th fibonacci number is {result1}")

  result2 = fibonacci2(n)
  print(f"The {n}th fibonacci number is {result2}")
