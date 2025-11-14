# Generate all binary substrings of a given length
# Difficulty: Medium

'''
Given an integer N , Print all binary strings of size N which do not contain consecutive 1s.

A binary string is that string which contains only 0 and 1.

Example 1:

Input:
N = 3
Output:
000 , 001 , 010 , 100 , 101
Explanation:
None of the above strings contain consecutive 1s. "110" is not an answer as it has '1's occuring consecutively. 
Your Task:

You don't need to read input or print anything. Your task is to complete the function generateBinaryStrings() which takes an integer N as input and returns a list of all valid binary strings in lexicographically increasing order.

Expected Time Complexity: O(2N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 20
'''

class Solution:
  def generateBinaryStrings(self, N):
    result = []

    def backtrack(current_string, last_char):
      if len(current_string) == N:
        result.append(current_string)
        return
      
      backtrack(current_string + '0', '0')
      
      if last_char != '1':
        backtrack(current_string + '1', '1')

    backtrack('', '')
    return result
  
if __name__ == "__main__":
  N = 3
  solution = Solution()
  result = solution.generateBinaryStrings(N)
  print(result)

