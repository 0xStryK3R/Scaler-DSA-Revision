class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def generate(self, cur_idx, cur_arr):
        if cur_idx == self.N:
            self.ans.append(" ".join(cur_arr))
            return

        wrd = ""
        for i in range(cur_idx, self.N):
            wrd += self.A[i]
            if wrd in self.B:
                cur_arr.append(wrd)
                self.generate(i + 1, cur_arr)
                cur_arr.pop()

    def wordBreak(self, A, B):
        self.N = len(A)
        self.A = A
        self.B = set(B)

        self.ans = []
        self.generate(0, [])

        return self.ans
