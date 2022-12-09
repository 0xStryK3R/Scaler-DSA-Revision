class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        queue = [1, 2]
        for i in range(A):
            ans = queue.pop(0)
            queue.append(ans*10+1)
            queue.append(ans*10+2)
        
        ans = str(ans)
        return int(ans+ans[::-1])