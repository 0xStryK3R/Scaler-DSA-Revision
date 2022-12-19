from functools import lru_cache, reduce
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
    if k<0:
        return 0
    return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

@lru_cache
def ways(N, min_flag=False):
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
    if min_flag:
        return nCk(N-3, l-2) * ways(l, True) * ways(r) + nCk(N-3, l-1) * ways(l) * ways(r) + nCk(N-3, l) * ways(l) * ways(r, True)
    else:
        return nCk(N-1, l) * ways(l) * ways(r)

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return ways(len(A), A.count(min(A))==2)%(10**9+7)
