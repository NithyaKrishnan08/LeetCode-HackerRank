# Lemonade change

'''
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

 

Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
 

Constraints:

1 <= bills.length <= 105
bills[i] is either 5, 10, or 20.
'''
from typing import List

# TC: O(N)
# SC: O(1)
class Solution:
  def lemonadeChange(self, bills: List[int]) -> bool:
    nos_5 = 0
    nos_10 = 0

    n = len(bills)

    for i in range(n):
      if bills[i] == 5:
        nos_5 += 1
      elif bills[i] == 10:
        if nos_5 >= 1:
          nos_5 -= 1
          nos_10 += 1
        else:
          return False
      else:
        if nos_10 >= 1 and nos_5 >= 1:
          nos_10 -= 1
          nos_5 -=1
        elif nos_5 >= 3:
          nos_5 -= 3
        else:
          return False
        
    return True
  
if __name__ == "__main__":
  bills = [5,5,5,10,20]
  solution = Solution()
  result = solution.lemonadeChange(bills)
  print(result)
