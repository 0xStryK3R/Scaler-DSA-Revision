# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A = list(A)
        N = len(A)
        ans = []
        for i in range(N-1):
            min_val_idx = i
            for j in range(i + 1, N):
                if A[j] < A[min_val_idx]:
                    min_val_idx = j
            A[i], A[min_val_idx] = A[min_val_idx], A[i]
            ans.append(min_val_idx)
        return ans
