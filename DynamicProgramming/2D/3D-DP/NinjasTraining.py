# Ninja's Training

'''
Problem Statement: A Ninja has an ‘N’ Day training schedule. He has to perform one of these three activities (Running, Fighting Practice, or Learning New Moves) each day. There are merit points associated with performing an activity each day. The same activity can’t be performed on two consecutive days. We need to find the maximum merit points the ninja can attain in N Days.

We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of specific activity on that particular day. Our task is to calculate the maximum number of merit points that the ninja can earn.
'''

# Recursion
def ninjaTraining0(day, last_task, points):
  no_tasks = 3
  if day == 0:
    max_point = 0
    for i in range(no_tasks):
      if i != last_task:
        max_point = max(max_point, points[0][i])
    return max_point
  
  max_point = 0
  for i in range(no_tasks):
    if i != last_task:
      merit_points = points[day][i] + ninjaTraining0(day - 1, i, points)
      max_point = max(max_point, merit_points)
  return max_point

# Memoization
def ninjaTraining1_util(day, last_task, points, dp):
  # Check if the result for this day and last task is already computed
  if dp[day][last_task] != -1:
    return dp[day][last_task]
  
  # Base case: When we reach day 0, return the maximum point 
  no_tasks = 3
  if day == 0:
    max_point = 0
    for i in range(no_tasks):
      if i != last_task:
        max_point = max(max_point, points[0][i])
    dp[day][last_task] = max_point
    return dp[day][last_task]
  
  max_point = 0
  for i in range(no_tasks):
    if i != last_task:
      merit_points = points[day][i] + ninjaTraining1_util(day - 1, i, points, dp)
      max_point = max(max_point, merit_points)
  
  dp[day][last_task] = max_point
  return dp[day][last_task]

def ninjaTraining1(points):
  n = len(points)
  dp = [[-1 for j in range(4)] for i in range(n)]
  return ninjaTraining1_util(n - 1, 3, points, dp)

#  Tabulation - Bottom to Up
# Time Complexity: O(N)
# Space Complexity: O(N)
def ninjaTraining2_util(n, points, dp):
  n = len(points)
  if n == 0:
    return 0

  dp[0][0] = max(points[0][1], points[0][2])
  dp[0][1] = max(points[0][0], points[0][2])
  dp[0][2] = max(points[0][0], points[0][1])
  dp[0][3] = max(points[0])
  
  for day in range(1, n):
    for last in range(4):
      dp[day][last] = 0
      for task in range(3):
        if task != last:
          merit_points = points[day][task] + dp[day - 1][task]
          dp[day][last] = max(dp[day][last], merit_points)
  
  return dp[n - 1][3]

def ninjaTraining2(points):
  n = len(points)
  dp = [[-1 for j in range(4)] for i in range(n)]
  return ninjaTraining2_util(n, points, dp)

# Space Optimization
# Time Complexity: O(N)
# Space Complexity: O(1)
def ninjaTraining3(points):
  n = len(points)
  prev = [0] * 4

  prev[0] = max(points[0][1], points[0][2])
  prev[1] = max(points[0][0], points[0][2])
  prev[2] = max(points[0][0], points[0][1])
  prev[3] = max(points[0])
  
  for day in range(1, n):
    temp = [0] * 4
    for last in range(4):
      temp[last] = 0
      for task in range(3):
        if task != last:
          merit_points = points[day][task] + prev[task]
          temp[last] = max(temp[last], merit_points)
  
    prev = temp

  return prev[3]

if __name__ == "__main__":
  points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
  n = len(points)
  no_tasks = 3 # 3 signifies none of the tasks are performed
  
  # Recursion solution
  # result = ninjaTraining0(n - 1, no_tasks, points)
  # print(result)

  # Memoization 
  # result = ninjaTraining1(points)
  # print(result)

  # Tabulation 
  # result = ninjaTraining2(points)
  # print(result)

  # Space Optimization 
  result = ninjaTraining3(points)
  print(result)
