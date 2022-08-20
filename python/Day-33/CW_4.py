class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        m = 10**9 + 7
        rem_dict = {}
        ans = 0

        for num in A:
            rem = num % B
            rem_opp = (B - rem) % B

            if rem_opp in rem_dict:
                ans = (ans + rem_dict[rem_opp]) % m

            rem_dict.setdefault(rem, 0)
            rem_dict[rem] += 1

        return ans
