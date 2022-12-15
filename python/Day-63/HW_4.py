class TrieNode:
    def __init__(self, b):
        self.bit = [None]*2
        self.val = b
        self.cnt = 0

    def set_next(self, i, nxt):
        self.bit[i] = nxt


def intToBinary(k):
    bin = [0] * 20
    i = 0
    while(k > 0):
        bin[i] = k % 2
        k = k // 2
        i = i + 1
    bin.reverse()
    return bin


def insertValue(p, root):
    V = intToBinary(p)
    curr = TrieNode(1)
    curr.bit = root.bit
    curr.val = root.val
    curr.cnt = curr.cnt
    for i in range(20):
        if (curr.bit[V[i]] == None):
            curr.bit[V[i]] = TrieNode(V[i])
        curr = curr.bit[V[i]]
        curr.cnt = curr.cnt + 1
    return


def query(p, k, root):
    P = intToBinary(p)
    K = intToBinary(k)
    curr = TrieNode(1)
    curr.bit = root.bit
    curr.val = root.val
    curr.cnt = curr.cnt
    ans = 0
    i = 0
    while(i < 20 and curr != None):
        if (K[i] == 0):
            if (P[i] == 1):
                curr = curr.bit[1]
            else:
                curr = curr.bit[0]
        else:
            if (P[i] == 1):
                if (curr.bit[1] != None):
                    ans = ans + curr.bit[1].cnt
                curr = curr.bit[0]
            else:
                if (curr.bit[0] != None):
                    ans = ans + curr.bit[0].cnt
                curr = curr.bit[1]
        i = i + 1

    if (curr != None):
        ans = ans + curr.cnt
    return ans


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if (len(A) == 0):
            return 0
        root = TrieNode(-1)
        insertValue(0, root)
        k = 0
        res = 0
        for i in range(len(A)):
            k = k ^ A[i]
            res += query(k, B - 1, root)
            insertValue(k, root)
        return int(res % (1e9+7))