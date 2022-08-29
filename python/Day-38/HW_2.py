def get_all_squares(N):
    squre_set = set()
    i = 1
    while i * i <= N:
        squre_set.add(i * i)
        i += 1
    return squre_set


class Solution:
    # @param A : list of integers
    # @return an integer
    def generate(self, cur_idx, cur_arr):
        if len(cur_arr) == self.N:
            self.cnt += 1
            return

        for k in self.freq_arr:
            if self.freq_arr[k]:
                if cur_arr:
                    if (cur_arr[-1] + k) not in self.squre_set:
                        continue

                self.freq_arr[k] -= 1
                cur_arr.append(k)

                self.generate(cur_idx + 1, cur_arr)

                cur_arr.pop()
                self.freq_arr[k] += 1

    def solve(self, A):
        self.squre_set = get_all_squares(sum(A))
        self.N = len(A)
        if self.N == 1:
            return int(A[0] in self.squre_set)

        freq_arr = {}
        for num in A:
            freq_arr[num] = freq_arr.get(num, 0) + 1

        self.freq_arr = freq_arr
        self.cnt = 0

        self.generate(0, [])

        return self.cnt
