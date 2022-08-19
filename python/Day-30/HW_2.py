# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x: (x.start, x.end))
        cur_int = intervals[0]
        ans = []
        for next_int in intervals:
            if next_int.start<=cur_int.end:
                if next_int.end>cur_int.end:
                    cur_int.end = next_int.end
            else:
                ans.append(cur_int)
                cur_int = next_int
        ans.append(cur_int)
        return ans