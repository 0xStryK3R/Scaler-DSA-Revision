# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        return [i if (i % 3 and i % 5) else str(str('' if i % 3 else 'Fizz')+str('' if i % 5 else 'Buzz')) for i in range(1, A+1)]
