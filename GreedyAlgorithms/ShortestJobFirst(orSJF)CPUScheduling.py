# Shortest Job First (or SJF) CPU Scheduling -> scheduling policy that selects the waiting process with the smallest execution time to execute next

'''
Problem Statement: Given a list of job durations representing the time it takes to complete each job. Implement the Shortest Job First algorithm to find the average waiting time for these jobs.

 Example 1:
                Input:jobs = [3, 1, 4, 2, 5]
                
                Output: 4           
                Explanation: 
                
The first job that will be executed is of duration 1 and the waiting time for it will be 0.
After the first job, the next shortest job with a duration of 2 will be executed with a waiting time of 1.
Following the completion of the first two jobs, the next shortest job with a duration of 3 will be executed with a waiting time of 3 (1 + 2).
Then, the job with a duration of 4 will be executed with a waiting time of 6 (1 + 2 + 3).
Finally, the job with the longest duration of 5 will be executed with a waiting time of 10 (1 + 2 + 3 + 4).

                Hence, the average waiting time is calculated as (0 + 1 + 3 + 6 + 10) / 5 = 20 / 5 = 4.
'''

# TC: O(N) + O(N log N)
# SC: O(1)
def shortest_job_first(jobs):
  n = len(jobs)
  jobs.sort()
  time_consumed = 0
  wait_time = 0

  for i in range(n):
    wait_time += time_consumed
    time_consumed += jobs[i]

  avg_time = wait_time // n

  return avg_time

if __name__ == "__main__":
  jobs = [4, 3, 7, 1, 2]
  result = shortest_job_first(jobs)
  print(result)