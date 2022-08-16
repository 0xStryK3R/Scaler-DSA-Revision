# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        pair_sum_hash = {}
        idx_pair_sum = {}
        N = len(A)
        ans_list = []
        for i in range(N):
            for j in range(i+1, N):
                pair_sum = A[i] + A[j]
                if pair_sum in (idx_pair_sum.get(i, set()) | idx_pair_sum.get(j, set())):
                    continue
                idx_pair_sum.setdefault(i, set())
                idx_pair_sum.setdefault(j, set())
                idx_pair_sum[i].add(pair_sum)
                idx_pair_sum[j].add(pair_sum)

                if pair_sum in pair_sum_hash:
                    ans_list.append(pair_sum_hash[pair_sum]+[i, j])
                else:
                    pair_sum_hash[pair_sum] = [i, j]

        if ans_list:
            ans_list.sort()
            return ans_list[0]
        return []
