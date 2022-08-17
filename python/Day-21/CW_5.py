class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)

        left_odd_ps = [0]
        left_even_ps = [0]

        right_odd_ps = [0]
        right_even_ps = [0]

        for i in range(N):
            if i & 1:
                left_odd_ps.append(left_odd_ps[-1] + A[i])
                left_even_ps.append(left_even_ps[-1])
            else:
                left_even_ps.append(left_even_ps[-1] + A[i])
                left_odd_ps.append(left_odd_ps[-1])

        for i in range(N - 1, -1, -1):
            if i & 1:
                right_odd_ps.append(right_odd_ps[-1] + A[i])
                right_even_ps.append(right_even_ps[-1])
            else:
                right_even_ps.append(right_even_ps[-1] + A[i])
                right_odd_ps.append(right_odd_ps[-1])

        right_odd_ps = right_odd_ps[::-1]
        right_even_ps = right_even_ps[::-1]

        cnt = 0

        for i in range(N):
            odd_sum = left_odd_ps[i] + right_even_ps[i + 1]
            even_sum = left_even_ps[i] + right_odd_ps[i + 1]

            if odd_sum == even_sum:
                cnt += 1

        return cnt
