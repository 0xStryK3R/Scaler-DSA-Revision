# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


def is_prime(num):
    if num < 2:
        return False
    i = 2
    while(i*i <= num):
        if not num % i:
            return False
        i += 1
    return True


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return len(list(filter(is_prime, A)))
