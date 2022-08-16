# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        N = len(A)
        for i in range(B):
            min_val_idx = i
            for j in range(i + 1, N):
                if A[j] < A[min_val_idx]:
                    min_val_idx = j
            A[i], A[min_val_idx] = A[min_val_idx], A[i]

        return A[i]
