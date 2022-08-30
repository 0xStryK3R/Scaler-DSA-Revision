class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def generate(self, cur_idx, cur_arr, cur_sum):
        if not cur_sum:
            self.ans.append(cur_arr.copy())
            return

        if cur_idx == self.N or cur_sum < 0:
            return

        for i in range(cur_idx, self.N):
            num = self.A[i]

            cur_arr.append(num)
            self.generate(i, cur_arr, cur_sum - num)
            cur_arr.pop()

    def combinationSum(self, A, B):
        A = sorted(list(set(A)))
        self.N = len(A)
        self.A = A
        self.ans = []
        self.generate(0, [], B)

        return self.ans
