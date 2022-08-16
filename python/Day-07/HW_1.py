# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        A = list(A)[::-1]
        B = list(B)[::-1]
        if len(A) > len(B):
            A, B = B, A

        B += ['0']
        A += ['0']*(len(B)-len(A))
        carry = '0'
        for i in range(len(A)):
            if A[i] == B[i]:
                B[i], carry = carry, B[i]
            else:
                if carry == '1':
                    B[i] = '0'
                else:
                    B[i] = '1'

        if B[-1] == '0':
            B = B[:-1]

        return ''.join(B[::-1])
