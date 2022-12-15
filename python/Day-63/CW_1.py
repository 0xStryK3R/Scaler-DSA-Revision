class TrieNode:
    def __init__(self):
        self.is_end = False
        self.child = {}
        self.freq = 0


def insert(trie, s):
    p = trie
    for ch in s:
        p.freq += 1
        if not p.child.get(ch, False):
            p.child[ch] = TrieNode()
        p = p.child[ch]
    p.freq += 1
    p.is_end = True


def create_trie(A):
    trie = TrieNode()
    for s in A:
        insert(trie, s)
    return trie


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        trie = create_trie(A)
        ans = []
        for word in A:
            min_prefix = ""
            p = trie
            for ch in word:
                if p.freq == 1:
                    break
                min_prefix += ch
                p = p.child[ch]
            ans.append(min_prefix)
        return ans
