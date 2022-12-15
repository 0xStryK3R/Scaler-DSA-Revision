class TrieNode:
    def __init__(self):
        self.is_end = False
        self.child = {}


def insert(trie, s):
    p = trie
    for ch in s:
        if not p.child.get(ch, False):
            p.child[ch] = TrieNode()
        p = p.child[ch]
    p.is_end = True


def create_trie(A):
    trie = TrieNode()
    for s in A:
        insert(trie, s)
    return trie


def max_dist(trie, num1):
    num2 = []
    alt_ch_map = {"0": "1", "1": "0"}
    for ch in num1:
        alt_ch = alt_ch_map[ch]
        if alt_ch in trie.child:
            num2.append(alt_ch)
            trie = trie.child[alt_ch]
        else:
            num2.append(ch)
            trie = trie.child[ch]

    return "".join(num2)


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_len = len(bin(max(A)))
        B = []
        for num in A:
            B.append("0" * (max_len - len(bin(num))) + bin(num)[2:])

        trie = create_trie(B)
        max_xor = 0

        for num1 in B:
            num2 = max_dist(trie, num1)
            max_xor = max(max_xor, int(num1, 2) ^ int(num2, 2))

        return max_xor
