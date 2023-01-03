class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def ispossible(self, cur_idx, cur_size, cur_sum):
        if cur_size == 0:
            return abs(cur_sum) < 1e-6

        if cur_idx == len(self.A):
            return False

        key = (cur_idx, cur_size, cur_sum)
        if not key in self.cache:
            sol = self.ispossible(
                cur_idx + 1, cur_size - 1, cur_sum - self.A[cur_idx]
            ) or self.ispossible(cur_idx + 1, cur_size, cur_sum)
            self.cache[key] = sol

        return self.cache[key]

    def avgset(self, A):
        A = sorted(A)
        self.A = A
        avg = float(sum(A)) / float(len(A))

        I = None
        Total = None
        for cur_size in range(1, len(A) // 2 + 1):
            self.cache = {}
            if self.ispossible(0, cur_size, cur_size * avg):
                I = cur_size
                Total = cur_size * avg
                break
        if not I:
            return []

        a = []
        b = []
        for j in range(len(A)):
            if self.ispossible(j + 1, I - 1, Total - A[j]):
                a.append(A[j])
                I -= 1
                Total -= A[j]
            else:
                b.append(A[j])

        return [a, b]
