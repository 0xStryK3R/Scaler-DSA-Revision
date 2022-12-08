class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        md_stack = [A[0]]
        ans = 0

        for num in A[1:]:
            while md_stack and md_stack[-1] < num:
                ans = max(ans, num ^ md_stack.pop())
            if md_stack:
                ans = max(ans, num ^ md_stack[-1])
            md_stack.append(num)

        return ans
