# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        freq_hash = {}
        for num in A:
            freq_hash[num] = freq_hash.get(num, 0) + 1

        ans = []

        for num in B:
            if num in freq_hash:
                freq_hash[num] -= 1
                if not freq_hash[num]:
                    freq_hash.pop(num)
                ans.append(num)

        return ans
