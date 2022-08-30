class Solution:
    # @param A : string
    # @return a list of list of strings
    def generate(self, cur_idx, cur_ans):
        if cur_idx == self.N:
            self.ans.append(cur_ans.copy())
            return

        fwd = ""
        rev = ""
        for i in range(cur_idx, self.N):
            ch = self.A[i]
            fwd += ch
            rev = ch + rev
            if fwd == rev:
                cur_ans.append(fwd)
                self.generate(i + 1, cur_ans)
                cur_ans.pop()

    def partition(self, A):
        self.N = len(A)
        self.A = A

        self.ans = []
        self.generate(0, [])

        return self.ans
