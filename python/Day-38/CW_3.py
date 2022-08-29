class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def generate(self, cur_idx, cur_sum, cnt):
        if cnt == self.B:
            if cur_sum <= 1000:
                self.ans += 1
            return

        if cur_idx == self.N or cur_sum > 1000:
            return

        self.generate(cur_idx + 1, cur_sum, cnt)

        self.generate(cur_idx + 1, cur_sum + self.A[cur_idx], cnt + 1)

    def solve(self, A, B):
        self.ans = 0
        self.A = A
        self.B = B
        self.N = len(A)

        self.generate(0, 0, 0)

        return self.ans
