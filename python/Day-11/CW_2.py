# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min_A, max_A = min(A), max(A)
        min_pos, max_pos = A.index(min(A)), A.index(max(A))

        N = len(A)

        ans = abs(min_pos - max_pos) + 1

        minA = min(A)
        maxA = max(A)

        for i in range(min(min_pos, max_pos) + 1, N):
            if A[i] == min_A:
                min_pos = i
                ans = min(ans, abs(min_pos - max_pos) + 1)

            if A[i] == max_A:
                max_pos = i
                ans = min(ans, abs(min_pos - max_pos) + 1)

        return ans
