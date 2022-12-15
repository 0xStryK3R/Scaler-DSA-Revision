class TrieNode:
    def __init__(self):
        self.is_end = False
        self.child = {}
        self.index = None


def insert(trie, s, i):
    p = trie
    for ch in s:
        if not p.child.get(ch, False):
            p.child[ch] = TrieNode()
        p = p.child[ch]
    p.index = i
    p.is_end = True


def create_trie(A):
    trie = TrieNode()
    for i, s in enumerate(A):
        insert(trie, s, i)
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

    return "".join(num2), trie.index


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        B = [0]
        for num in A:
            B.append(B[-1] ^ num)

        max_len = len(bin(max(B)))
        C = []
        for num in B:
            C.append("0" * (max_len - len(bin(num))) + bin(num)[2:])

        trie = create_trie(C)
        max_xor = max(A)
        idx = A.index(max_xor)
        ans = [idx, idx + 1]

        for i1, num1 in enumerate(C):
            num2, i2 = max_dist(trie, num1)
            cur_xor = int(num1, 2) ^ int(num2, 2)

            if cur_xor > max_xor:
                max_xor = cur_xor
                ans = sorted([i1, i2])
            elif cur_xor == max_xor:
                if (
                    not ans
                    or abs(i2 - i1) < ans[1] - ans[0]
                    or (abs(i2 - i1) == ans[1] - ans[0] and min([i1, i2]) < ans[0])
                ):
                    ans = sorted([i1, i2])

        return ans[0] + 1, ans[1]
