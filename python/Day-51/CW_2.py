class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        stack = []

        for ch in A:
            if stack and stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)
        
        return ''.join(stack)
