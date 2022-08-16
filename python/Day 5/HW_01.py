# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 08:53:28 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        A.sort()
        l = 0
        r = N-1

        while(l+1 < N and A[l] == A[l+1]):
            l += 1

        if l + 1 == N:
            return 0

        while(r > 0 and A[r] == A[r-1]):
            r -= 1

        return 0 if l == r else r-l-1
