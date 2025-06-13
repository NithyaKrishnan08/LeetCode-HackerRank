# Online Stock Plan -> Maximum consecutive days for which the stock price was less than or equal to current days

'''
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.
 

Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
'''
# Brute force solution
# TC: O(No. of days)
# SC: O(total no. of next calls)
class StockSpanner1:
  def __init__(self):
    self.arr = []

  def next(self, price: int) -> int:
    self.arr.append(price)
    count = 1
    for i in range(len(self.arr) - 2, -1, -1):
      if self.arr[i] <= price:
        count += 1
      else:
        break

    return count
  
# Optimal solution
# TC: O(2N)
# SC: O(N)
class StockSpanner:
  def __init__(self):
    self.stack = []
    self.idx = -1

  def next(self, price: int) -> int:
    self.idx += 1
    
    while self.stack and self.stack[-1][0] <= price:
      self.stack.pop()

    ans = self.idx - (-1 if not self.stack else self.stack[-1][1])

    self.stack.append((price, self.idx))
    
    return ans

if __name__ == "__main__":
  nums = [1,3,-1,-3,5,3,6,7]
  k = 3
  stockSpanner = StockSpanner()

  result1 = stockSpanner.next(100)
  print(result1)

  result2 = stockSpanner.next(80)
  print(result2)

  result3 = stockSpanner.next(60)
  print(result3)

  result4 = stockSpanner.next(70)
  print(result4)

  result5 = stockSpanner.next(60)
  print(result5)

  result6 = stockSpanner.next(75)
  print(result6)

  result7 = stockSpanner.next(85)
  print(result7)