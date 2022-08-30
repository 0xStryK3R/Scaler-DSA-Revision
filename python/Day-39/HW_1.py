class Solution:
    # @param A : string
    # @return a list of strings
    def generate(self, cur_idx, cur_bal, cur_str):
        if cur_bal < 0:
            return

        if cur_idx == self.N:
            if not cur_bal:
                if len(cur_str) > self.max_len:
                    self.max_len = len(cur_str)
                    self.ans = []
                elif len(cur_str) < self.max_len:
                    return

                if cur_str not in self.ans:
                    self.ans.append(cur_str)
            return

        self.generate(cur_idx + 1, cur_bal, cur_str)

        ch = self.A[cur_idx]
        cur_str += ch
        if ch == "(":
            cur_bal += 1
        if ch == ")":
            cur_bal -= 1

        self.generate(cur_idx + 1, cur_bal, cur_str)

    def solve(self, A):
        self.N = len(A)
        self.A = A
        self.ans = []
        self.max_len = 0

        self.generate(0, 0, "")

        return self.ans
