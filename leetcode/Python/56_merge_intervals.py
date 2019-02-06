import numpy as np

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        ans = [intervals[0]]
        j = 0
        for i in range(1, len(intervals)):
            if intervals[i].start <= ans[j].end:
                ans[j].end = intervals[i].end
            else:
                ans.append(intervals[i])
                j += 1
        return ans

if __name__ == "__main__":
    Intervals = []
    # Intervals.append(Interval(1, 3))
    # Intervals.append(Interval(2, 6))
    # Intervals.append(Interval(8, 10))
    # Intervals.append(Interval(15, 18))

    Intervals.append(Interval(1, 4))
    Intervals.append(Interval(4, 5))
    
    sol = Solution()
    ans = sol.merge(Intervals)
    for ele in ans:
        print (ele.start, ele.end)