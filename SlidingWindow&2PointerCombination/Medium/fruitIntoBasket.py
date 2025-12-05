# Fruit into baskets
# https://leetcode.com/problems/fruit-into-baskets/description/
# Leetcode: 904
# Difficulty: Medium

'''
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
'''
# Max length of subarray with atmost 2 types of fruits
from typing import List
from collections import deque

class Solution:
  #  Brute force solution
  # T: O(N^2)
  # S: O(3)
  def totalFruit1(self, fruits: List[int]) -> int:
    n = len(fruits)
    max_len = 0
    for i in range(n):
      seen_fruits = set()
      for j in range(i, n):
        seen_fruits.add(fruits[j])
        if len(seen_fruits) <= 2:
          max_len = max(max_len, j - i + 1)
        else:
          break
    
    return max_len
  
  # Optimal solution
  # T: O(N)
  # S: O(3)
  def totalFruit(self, fruits: List[int]) -> int:
    n = len(fruits)
    max_len = 0
    fruit_freq = {}

    left, right = 0, 0
    for right in range(n):
      fruit_freq[fruits[right]] = fruit_freq.get(fruits[right], 0) + 1
      
      while len(fruit_freq) > 2:
        fruit_freq[fruits[left]] -= 1
        if fruit_freq[fruits[left]] == 0:
          del fruit_freq[fruits[left]]
        left += 1

      max_len = max(max_len, right - left + 1)
    
    return max_len
  

if __name__ == "__main__":
  fruits = [1,2,3,2,2]

  solution = Solution()
  result = solution.totalFruit(fruits)
  print(result)
        