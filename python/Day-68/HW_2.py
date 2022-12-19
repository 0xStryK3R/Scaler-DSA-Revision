from functools import lru_cache
import sys
sys.setrecursionlimit = 10**6

@lru_cache
def is_prime(n):
    if n==1:
        return 0
    i = 2
    while(i*i<=n):
        if not n%i:
            return 0
        i += 1
    return 1

class Solution:
    def build(self, idx, st, end):
        if st==end:
            self.seg_tree[idx] = is_prime(self.A[st])
            return
        mid = (st+end)>>1
        self.build(2*idx+1, st, mid)
        self.build(2*idx+2, mid+1, end)
        self.seg_tree[idx] = self.seg_tree[2*idx+1] + self.seg_tree[2*idx+2]
        
    def query(self, idx, st, end, L, R):
        if(R<st or L>end): #No Overlap
            return 0
        if(L<=st and R>=end): #Complete Overlap
            return self.seg_tree[idx]
        #Partial Overlap
        mid = (st+end)>>1
        qL = self.query(2*idx+1, st, mid, L, R)
        qR = self.query(2*idx+2, mid+1, end, L, R)
        return qL + qR
        
    def update(self, idx, st, end, uidx, val):
        if st==end==uidx:
            self.seg_tree[idx] = is_prime(val)
            return
        
        mid = (st+end)>>1
        if uidx<=mid:
            self.update(2*idx+1, st, mid, uidx, val)
        else:
            self.update(2*idx+2, mid+1, end, uidx, val)
        self.seg_tree[idx] = self.seg_tree[2*idx+1] + self.seg_tree[2*idx+2]
        
    def solve(self, A, B, C, D):
        N = len(A)
        st = idx = 0
        end = N - 1
        self.A = A
        self.seg_tree = [None]*(4*N)
        self.build(idx, st, end)

        ans = []
        
        for act, x, y in zip(B, C, D):
            if act=='A':
                ans.append(self.query(idx, st, end, x-1, y-1))
            else:
                self.update(idx, st, end, x-1, y)
        
        return ans
