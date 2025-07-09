# Frog Jump

'''
Problem Statement:

Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

Examples

Examples:


'''
# Recursion
def frogJump0(index, height):
  if(index == 0):
    return 0
  jump_two = float('inf')
  jump_one = frogJump0(index - 1, height) + abs(height[index] - height[index - 1])
  if index > 1:
    jump_two = frogJump0(index - 2, height) + abs(height[index] - height[index - 2])
  
  result = min(jump_one, jump_two)
  return result

# Memoization - Top - Bottom
# Time Complexity: O(N)
# Space Complexity : O(2N)

# 1. Write in terms of index
# 2. Do all stuff on the indexes
# 3. Take the minimum of all the stuffs
# Minimum energy required to reach (n - 1) from 0
def frogJump1(index, height, dp):
  if(index == 0):
    return 0
  
  if dp[index] != -1:
    return dp[index]
  
  jump_two = float('inf')
  jump_one = frogJump1(index - 1, height, dp) + abs(height[index] - height[index - 1])
  if index > 1:
    jump_two = frogJump1(index - 2, height, dp) + abs(height[index] - height[index - 2])
  
  dp[index] = min(jump_one, jump_two)
  return dp[index]

#  Tabulation - Bottom to Up
# Time Complexity: O(N)
# Space Complexity: O(N)
def frogJump2(height):
  n = len(height)
  dp = [-1] * n
  dp[0] = 0

  for index in range(1, n):
    jump_two = float('inf')
    jump_one = dp[index - 1] + abs(height[index] - height[index - 1])
    if index > 1:
      jump_two = dp[index - 2] + abs(height[index] - height[index - 2])
    
    dp[index] = min(jump_one, jump_two)
  return dp[n - 1]

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
  dp = [-1] * n
  # Recursion solution
  # result = frogJump0(n - 1, height)
  # print(result)

  # Memoization 
  # result = frogJump1(n - 1, height, dp)
  # print(result)

  # Tabulation 
  # result = frogJump2(height)
  # print(result)

  # Space Optimization 
  result = frogJump3(height)
  print(result)

  