class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = [A[0]]
        for num in A:
            if num != ans[-1]:
                ans.append(num)

        return ans
