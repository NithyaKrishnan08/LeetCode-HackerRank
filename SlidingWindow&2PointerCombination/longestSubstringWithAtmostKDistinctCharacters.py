# Longest Substring With At Most K Distinct Characters

'''
You are given string S of length N, and an integer K. Your task is to find the length of the longest substring that contains at most K distinct characters.

Input Format:
The first line contains an Integer 'T' which denotes the number of test cases/queries to be run. 
Then the test cases follow. 

The first line of input for each test case/query contains an integer K.

The second line of input for each test case/query contains a string S.
Output Format:
For each test case, print the length of the longest substring that contains at most K distinct characters.

Output for every test case will be printed in a separate line.
Note:
You do not need to print anything, it has already been taken care of. Just implement the function.
Constraints:
1 <= T <= 10
1 <= K <= 26
1 <= N <= 10^4

Time Limit: 1sec
'''

class Solution:
  # Brute Force Solution
  # T: O(N^2)
  # S: O(26)
  def lengthOfLongestSubstringWithAtmostKdistinct1(self, s: str, k: int) -> int:
    n = len(s)
    max_length = 0
    mpp = {}
    
    for i in range(n):
      mpp.clear()
      for j in range(i, n):
        mpp[s[j]] = mpp.get(s[j], 0) + 1

        if len(mpp) > 2:
          break

        max_length = max(max_length, j - i + 1)

    return max_length
  
  # Optimal solution - sliding window and 2 pointer
  # T: O(N)
  # S: O(1)
  def lengthOfLongestSubstringWithAtmostKdistinct(self, s: str, k: int) -> int:
    n = len(s)

    max_length = 0
    left, right = 0, 0
    mpp = {}

    for right in range(n):
      mpp[s[right]] = mpp.get(s[right], 0) + 1

      if len(mpp) > k:
        mpp[s[left]] -= 1
        if mpp[s[left]] == 0:
          del mpp[s[left]]
        left += 1
          
      max_length = max(max_length, right - left + 1)

    return max_length
  
if __name__ == "__main__":
  s = "aaabbccd"
  k = 2
  solution = Solution()
  result = solution.lengthOfLongestSubstringWithAtmostKdistinct(s, k)
  print(result)