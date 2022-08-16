# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        top = -1
        left = -1
        right = A
        bottom = A

        spiral_mat = [[None]*A for i in range(A)]

        i, j = 0, 0
        num = 1
        while(top < bottom and left < right):
            while(j < right):
                spiral_mat[i][j] = num
                num += 1
                j += 1
            j -= 1
            i += 1
            top += 1
            while(i < bottom):
                spiral_mat[i][j] = num
                num += 1
                i += 1
            i -= 1
            j -= 1
            right -= 1
            while(j > left):
                spiral_mat[i][j] = num
                num += 1
                j -= 1
            j += 1
            i -= 1
            bottom -= 1
            while(i > top):
                spiral_mat[i][j] = num
                num += 1
                i -= 1
            i += 1
            j += 1
            left += 1

        return spiral_mat
