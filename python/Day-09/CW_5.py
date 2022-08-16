# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = list(input().split())
    B = int(input())
    B = B % int(A[0])
    A = A[1:]

    print(' '.join((A[-B:]+A[:-B]))+' ')


if __name__ == '__main__':
    main()
