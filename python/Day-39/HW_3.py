class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def generate(self, cur_idx, cur_arr, cur_sum):
        if cur_sum == self.B:
            if cur_arr.copy() not in self.ans:
                self.ans.append(cur_arr.copy())
            return
        
        if cur_sum>self.B or cur_idx==self.N:
            return

        for i in range(cur_idx, self.N):
            num = self.A[i]
            cur_arr.append(num)
            self.generate(i + 1, cur_arr, cur_sum+num)
            cur_arr.pop()

    def combinationSum(self, A, B):
        A.sort()

        self.N = len(A)
        self.A = A
        self.B = B
        self.ans = []

        self.generate(0, [], 0)

        return self.ans