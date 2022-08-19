# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):

        start, end = sorted([newInterval.start, newInterval.end])

        start_ind = end_ind = -1

        for i, interval in enumerate(intervals):
            if interval.end >= start:
                start_ind = i
                if interval.start < start:
                    start = interval.start
                break

        if start_ind < 0:
            intervals.append(newInterval)
            return intervals

        for i in range(len(intervals) - 1, -1, -1):
            if intervals[i].start <= end:
                end_ind = i
                if intervals[i].end > end:
                    end = intervals[i].end
                break

        if end_ind < 0:
            ans = [newInterval]
            ans.extend(intervals)
            return ans

        ans = intervals[:start_ind]

        ans.append(Interval(start, end))

        ans.extend(intervals[end_ind + 1 :])

        return ans
