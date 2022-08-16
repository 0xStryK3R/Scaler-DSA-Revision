# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        month_dict = {m: str(i+1) for i, m in enumerate(
            ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}
        d, m, yyyy = A.split()
        dd = d[:-2]
        if len(dd) == 1:
            dd = '0' + dd
        mm = month_dict[m]
        if len(mm) == 1:
            mm = '0' + mm

        ans = yyyy + '-' + mm + '-' + dd

        return ans
