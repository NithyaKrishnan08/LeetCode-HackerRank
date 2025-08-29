# Number of Ways to Select Buildings
# https://leetcode.com/problems/number-of-ways-to-select-buildings/description/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
# Leetcode Problem 2222: Number of Ways to Select Buildings

'''
You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.

 

Example 1:

Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
Example 2:

Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
 

Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.
'''

class Solution:
  def numberOfWays(self, s: str) -> int:
    n = len(s)
    ans = 0

    for i in range(n):
      for j in range(i + 1, n):
        for k in range(j + 1, n):
          if (s[i] == '0' and s[j] == '1' and s[k] == '0') or (s[i] == '1' and s[j] == '0' and s[k] == '1'):
            ans += 1
    
    return ans
  
if __name__ == "__main__":
  s = Solution()
  print(s.numberOfWays("001101"))  # 6
  print(s.numberOfWays("11100"))   # 0
        