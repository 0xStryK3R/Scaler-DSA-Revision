# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        N = len(A)
        for i in range(N):
            A[i] += (A[A[i]] % N)*N
        for i in range(N):
            A[i] = (int)(A[i]/N)

        return A
