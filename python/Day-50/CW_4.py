class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        ball_stack = [B]
        for pass_val in C:
            if pass_val==0:
                ball_stack.pop()
            else:
                ball_stack.append(pass_val)
        
        return ball_stack[-1]