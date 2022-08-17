# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""

# Combinatorics Approach for resolving TLE in DP approach.
# Reference: https://towardsdatascience.com/understanding-combinatorics-number-of-paths-on-a-grid-bddf08e28384


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        # Optimisation, so that iteration is done for from larger of two numbers to m+n-2
        B, A = sorted([A, B])
        path = 1
        for i in range(A, (A + B - 1)):
            path = (path * i) // (i - A + 1)

        return path
