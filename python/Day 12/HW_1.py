# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        box_map = [[0]*3 for _ in range(3)]
        row_map = [0]*9
        col_map = [0]*9

        for i in range(9):
            for j in range(9):
                if A[i][j] == '.':
                    continue
                n = int(A[i][j])
                b = 1 << n
                if (box_map[i//3][j//3] >> n) & 1:
                    return 0
                if (row_map[i] >> n) & 1:
                    return 0
                if (col_map[j] >> n) & 1:
                    return 0
                box_map[i//3][j//3] |= b
                row_map[i] |= b
                col_map[j] |= b

        return 1
