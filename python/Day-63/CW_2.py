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


def check_dictionary(trie, word):
    for ch in word:
        if ch not in trie.child:
            return False
        trie = trie.child[ch]

    return trie.is_end


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):

        trie = create_trie(A)

        return [int(check_dictionary(trie, word)) for word in B]
