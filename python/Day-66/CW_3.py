class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        intervals = list(zip(A, B))

        intervals.sort(key=lambda x: (x[-1], -x[0]))

        prev = intervals[0]

        count = 0

        for cur in intervals[1:]:
            if cur[0] < prev[-1]:
                continue

            count += 1
            prev = cur

        return count + 1
