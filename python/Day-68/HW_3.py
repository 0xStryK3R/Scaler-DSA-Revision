def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y % 2:
            res = (res * x) % p
        y = y // 2
        x = (x * x) % p
    return res

def modInverse(a, m):
    return power(a, m - 2, m)

n = 0
class SegTree:
    bit = []
    mod = []

    def __init__(self, A):
        self.bit = [0] * (4 * len(A))
        self.mod = [0] * (4 * len(A))
        self.build(A, 0, len(A) - 1, 0)

    # build segment tree
    def build(self, A, start, end, ind):
        bit = self.bit
        mod = self.mod
        global n
        if start > end:
            return
        if start == end:
            bit[ind] = ord(A[start]) - ord("0")
            mod[ind] = bit[ind] * power(2, n - 1 - end, 3)
            return
        mid = (start + end) // 2
        self.build(A, start, mid, 2 * ind + 1)
        self.build(A, mid + 1, end, 2 * ind + 2)
        mod[ind] = (mod[2 * ind + 1] + mod[2 * ind + 2]) % 3

    # update to handle updates
    def update(self, ind, start, end, l, val):
        r = l
        bit = self.bit
        mod = self.mod
        global n
        if start > r or l > end or start > end:
            return
        if start >= l and end <= r:
            bit[ind] = 1
            mod[ind] = bit[ind] * power(2, n - 1 - end, 3)
            return
        mid = (start + end) // 2
        self.update(2 * ind + 1, start, mid, l, val)
        self.update(2 * ind + 2, mid + 1, end, l, val)
        mod[ind] = (mod[2 * ind + 1] + mod[2 * ind + 2]) % 3

    # find the sum from l to r
    def get(self, ind, start, end, l, r):
        bit = self.bit
        mod = self.mod
        global n
        if start > end or start > r or end < l:
            return 0
        if start >= l and end <= r:
            return mod[ind]
        mid = (start + end) // 2
        left = self.get(2 * ind + 1, start, mid, l, r)
        right = self.get(2 * ind + 2, mid + 1, end, l, r)
        return (left + right) % 3


class Solution:
    def solve(self, A, B):
        global n
        n = len(A)
        st = SegTree(A)
        ans = []
        for i in range(0, len(B)):
            if B[i][0] == 0:
                l = B[i][1] - 1
                r = B[i][2] - 1
                val = st.get(0, 0, n - 1, l, r)
                val = (val * modInverse(power(2, n - 1 - r, 3), 3)) % 3
                ans.append(val)
            else:
                st.update(0, 0, n - 1, B[i][1] - 1, 1)
                ans.append(-1)
        return ans