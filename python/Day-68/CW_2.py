import sys

sys.setrecursionlimit = 10**6


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def build(self, idx, st, end):
        if st == end:
            self.seg_tree[idx] = self.A[st]
            return
        mid = (st + end) >> 1
        self.build(2 * idx + 1, st, mid)
        self.build(2 * idx + 2, mid + 1, end)
        self.seg_tree[idx] = sum(self.seg_tree[2 * idx + 1], self.seg_tree[2 * idx + 2])

    def query(self, idx, st, end, L, R):
        if R < st or L > end:  # No Overlap
            return 0
        if L <= st and R >= end:  # Complete Overlap
            return self.seg_tree[idx]
        # Partial Overlap
        mid = (st + end) >> 1
        qL = self.query(2 * idx + 1, st, mid, L, R)
        qR = self.query(2 * idx + 2, mid + 1, end, L, R)
        return sum([qL, qR])

    def update(self, idx, st, end, uidx, val):
        if st == end == uidx:
            self.seg_tree[idx] += val
            if self.seg_tree[idx] < 0:
                self.seg_tree[idx] = 0
            return

        mid = (st + end) >> 1
        if uidx <= mid:
            self.update(2 * idx + 1, st, mid, uidx, val)
        else:
            self.update(2 * idx + 2, mid + 1, end, uidx, val)
        self.seg_tree[idx] = sum(
            [self.seg_tree[2 * idx + 1], self.seg_tree[2 * idx + 2]]
        )

    def solve(self, A, B):
        N = A
        st = idx = 0
        end = N - 1
        self.A = A
        self.seg_tree = [0] * (4 * N)

        ans = []

        for x, y, z in B:
            if x == 1:
                self.update(idx, st, end, y - 1, 1)
            elif x == 2:
                self.update(idx, st, end, y - 1, -1)
            else:
                ans.append(self.query(idx, st, end, y - 1, z - 1))

        return ans
