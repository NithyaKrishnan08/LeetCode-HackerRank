'''
You are given an array of heights of pile of boxes. You have to return the number of steps required to bring the height of entire pile to the same height as pile with minimum height. In one step, you can lower the tallest pile only to the next taller pile. You can adjust only one pile in a step even though 2 piles could be of same height. Following examples will illustrate this better,

Example 1:

Input: arrOfHeights = [150, 210, 210, 80, 110]
Output: 9
Explanation:
Step 1 [150, 150, 210, 80, 110]
Step 2 [150, 150, 150, 80, 110]
Step 3 [110, 150, 150, 80, 110]
Step 4 [110, 110, 150, 80, 110]
Step 5 [110, 110, 110, 80, 110]
Step 6 [80, 110, 110, 80, 110]
Step 7 [80, 80, 110, 80, 110]
Step 8 [80, 80, 80, 80, 110]
Step 9 [80, 80, 80, 80, 80]
Example 2:

Input: arrOfHeights = [843, 247]
Output: 1
Explanation:
Step 1 [247, 247]
Example 3:

Input: arrOfHeights = [2]
Output: 0
'''

# Pile of boxes
# Time Complexity: O(n log n + n)
# Space Complexity: O(1)
def minStepsToEqualHeight(arrOfHeights):
    if len(arrOfHeights) <= 1:
      return 0

    arrOfHeights.sort(reverse=True)
    steps = 0
    i = 0
    while i < len(arrOfHeights) - 1:
      if arrOfHeights[i + 1] < arrOfHeights[i]:
        steps += i + 1
      i += 1
    return steps

if __name__ == "__main__":
  arr = [150, 210, 210, 80, 110]
  result = minStepsToEqualHeight(arr)
  print(f"Minimum steps to equal height of piles: {result}")

      