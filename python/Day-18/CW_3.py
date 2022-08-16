# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        digit_cnt = 0
        while((int)(A/10**(digit_cnt))):
            digit_cnt += 1

        while(A):
            msd = (int)(A/10**(digit_cnt-1))
            lsd = A % 10
            if msd != lsd:
                return 0
            A = A % (10**(digit_cnt-1))
            A = (int)(A/10)
            digit_cnt -= 2

        return 1
