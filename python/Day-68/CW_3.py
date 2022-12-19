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
        self.seg_tree[idx] = self.seg_tree[2 * idx + 1] + self.seg_tree[2 * idx + 2]

    def update(self, idx, st, end, uidx, val):
        if st == end == uidx:
            self.seg_tree[idx] = 0
            return

        mid = (st + end) >> 1
        if uidx <= mid:
            self.update(2 * idx + 1, st, mid, uidx, val)
        else:
            self.update(2 * idx + 2, mid + 1, end, uidx, val)

        self.seg_tree[idx] = self.seg_tree[2 * idx + 1] + self.seg_tree[2 * idx + 2]

    def query(self, idx, st, end, val):
        if st == end:
            if self.seg_tree[idx] == val:
                return st
            return -2
        if self.seg_tree[idx] < val:
            return -2

        lc = self.seg_tree[2 * idx + 1]
        mid = (st + end) >> 1

        if lc >= val:
            return self.query(2 * idx + 1, st, mid, val)

        return self.query(2 * idx + 2, mid + 1, end, val - lc)

    def solve(self, A, B):
        N = A
        st = idx = 0
        end = N - 1
        self.A = [1] * A
        self.seg_tree = [None] * (4 * N)
        self.build(idx, st, end)

        ans = []

        for x, y in B:
            if x & 1:
                ans.append(self.query(idx, st, end, y) + 1)
            else:
                self.update(idx, st, end, y - 1, 0)
        return ans
