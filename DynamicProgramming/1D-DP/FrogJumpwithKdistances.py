# Frog Jump

'''
Prooblem Statement:

This is a follow-up question to “Frog Jump” discussed in the previous article. In the previous question, the frog was allowed to jump either one or two steps at a time. In this question, the frog is allowed to jump up to ‘K’ steps at a time. If K=4, the frog can jump 1,2,3, or 4 steps at every index.


'''
# Recursion
def frogJump0(index, height, k):
  if index == 0:
    return 0

  min_steps = float('inf')

  for j in range(1, k + 1):
    if index - j >= 0:
      jumps = frogJump0(index - j, height, k) + abs(height[index] - height[index - j])
      min_steps = min(min_steps, jumps)

  return min_steps

# Memoization - Top - Bottom
# Time Complexity: O(N * k)
# Space Complexity : O(N)

# 1. Write in terms of index
# 2. Do all stuff on the indexes
# 3. Take the minimum of all the stuffs
# Minimum energy required to reach (n - 1) from 0
def frogJump1_util(index, height, k, dp):
  if(index == 0):
    return 0
  
  if dp[index] != -1:
    return dp[index]
  
  min_steps = float('inf')
  for j in range(1, k + 1):
    if index - j >= 0:
      jumps = frogJump1_util(index - j, height, k, dp) + abs(height[index] - height[index - j])
      min_steps = min(min_steps, jumps)

  dp[index] = min_steps
  return dp[index]

def frogJump1(height, k):
  n = len(height)
  dp = [-1] * n
  return frogJump1_util(n - 1, height, k, dp)

#  Tabulation - Bottom to Up
# Time Complexity: O(N)
# Space Complexity: O(N)
def frogJump2_util(n, height, k, dp):
  n = len(height)
  dp[0] = 0

  for index in range(1, n):
    min_steps = float('inf')
    for j in range(1, k + 1):
      if index - j >= 0:
        jumps = dp[index - j] + abs(height[index] - height[index - j])
        min_steps = min(min_steps, jumps)
    
    dp[index] = min_steps
  return dp[n - 1]

def frogJump2(height, k):
  n = len(height)
  dp = [-1] * n
  return frogJump2_util(n, height, k, dp)

# Space Optimization
# Time Complexity: O(N)
# Space Complexity: O(1)
def frogJump3(height):
  n = len(height)
  prev2_i = 0
  prev1_i = 0

  if n == 0:
    return 0

  for index in range(1, n):
    jump_two = float('inf')
    jump_one = prev1_i + abs(height[index] - height[index - 1])
    if index > 1:
      jump_two = prev2_i + abs(height[index] - height[index - 2])
    
    current_i = min(jump_one, jump_two)
    prev2_i = prev1_i
    prev1_i = current_i
  
  return prev1_i

if __name__ == "__main__":
  height = [30, 10, 60, 10, 60, 50]
  n = len(height)
  k = 2

  # Recursion solution
  # result = frogJump0(n - 1, height, k)
  # print(result)

  # Memoization 
  # result = frogJump1(height, k)
  # print(result)

  # Tabulation 
  result = frogJump2(height, k)
  print(result)

  # Space Optimization 
  # result = frogJump3(height)
  # print(result)

  