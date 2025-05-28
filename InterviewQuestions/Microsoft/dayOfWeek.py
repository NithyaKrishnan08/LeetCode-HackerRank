'''
Given current day as day of the week and an integer K, the task is to find the day of the week after K days.

Example 1:
Input:
day = “Monday”
K = 3
Output: Thursday

Example 2:
Input:
day = “Tuesday”
K = 101
Output: Friday
'''

def day_of_week(day, K):
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  for i in range(len(days)):
    if days[i] == day:
      index = i

  return days[(index + K) % 7]

if __name__ == "__main__":
  day = "Saturday"
  K = 3

  result = day_of_week(day, K)
  print(result)