class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        queue = ['1', '2', '3']
        top = 0

        ans = []

        for i in range(A):
            x = queue[i]
            ans.append(int(x))
            queue.extend([x+'1', x+'2', x+'3'])
        
        return ans
