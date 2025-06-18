# Job Sequencing
# delay the job
# Maximize the profit

'''
Problem Statement: You are given a set of N jobs where each job comes with a deadline and profit. The profit can only be earned upon completing the job within its deadline. Find the number of jobs done and the maximum profit that can be obtained. Each job takes a single unit of time and only one job can be performed at a time.

Examples

Example 1:

Input: N = 4, Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}

Output: 2 60

Explanation: The 3rd job with a deadline 1 is performed during the first unit of time .The 1st job is performed during the second unit of time as its deadline is 4.
Profit = 40 + 20 = 60

Example 2:

Input: N = 5, Jobs = {(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)}

Output: 2 127

Explanation: The  first and third job both having a deadline 2 give the highest profit. 
Profit = 100 + 27 = 127
'''
# TC: O(N log N) + O(N * maxDeadline)
# SC: O(maxDeadline)
class Job:
  def __init__(self, id, deadline, profit):
    self.id = id
    self.deadline = deadline
    self.profit = profit

class Solution:
  def jobScheduling(self, jobs):
    #  Converting array of tuples to Job objects
    jobs_arr = [Job(*x) for x in jobs]

    jobs_arr.sort(key=lambda x: x.profit, reverse = True)

    max_deadline = max(job.deadline for job in jobs_arr)

    slots = [-1] * (max_deadline + 1)
    countJobs = 0
    jobProfit = 0

    for i in range(len(jobs_arr)):
      for j in range(jobs_arr[i].deadline, 0, -1):
        if slots[j] == -1:
          slots[j] = i
          countJobs += 1
          jobProfit += jobs_arr[i].profit
          break

    return countJobs, jobProfit
  
if __name__ == "__main__":
  solution = Solution()
  jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
  countJobs, jobProfit = solution.jobScheduling(jobs)
  print(countJobs, jobProfit)