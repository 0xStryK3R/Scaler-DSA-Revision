MOD = 1000003
dp = [-1]*1000
dp[0] = dp[1] = 1

def fact(n):
    if dp[n] == -1:
        dp[n] = (n*fact(n-1))%MOD
    return dp[n]

class Solution:
	# @param A : string
	# @return an integer
    def findRank(self, A):
        N = len(A)

        ordered_string = sorted(list(A))

        i = 0
        rank = 1

        while(i<N):
            ch = A[i]
            ch_rank = ordered_string.index(ch)
            ordered_string.remove(ch)
            rank = (rank + (ch_rank*fact(N-i-1))%MOD)%MOD

            i += 1
        
        return rank
