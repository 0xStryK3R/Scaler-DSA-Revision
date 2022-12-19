from functools import lru_cache, reduce
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

@lru_cache
def ways(N):
    if N < 3:
        return 1
    
    h = len(bin(N))-2
    
    total_level_max_cnt = 2**h - 1
    last_level_max_cnt = 2**(h-1)
    deficit = total_level_max_cnt - N
    last_level_actual_cnt = last_level_max_cnt - deficit

    #To account for leaves
    if last_level_actual_cnt < last_level_max_cnt//2:
        l = last_level_actual_cnt
        r = 0
    else:
        l = last_level_max_cnt//2
        r = last_level_actual_cnt - l

    #To account for internal nodes
    l += (total_level_max_cnt - last_level_max_cnt - 1)//2
    r += (total_level_max_cnt - last_level_max_cnt - 1)//2
    
    return nCk(N-1, l) * ways(l) * ways(r)

class Solution:
	# @param A : integer
	# @return an integer
    def solve(self, A):
        return ways(A)%(10**9+7)