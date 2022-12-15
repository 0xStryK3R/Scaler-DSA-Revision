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

def get_freq(trie, s):
    min_freq = trie.freq
    for ch in s:
        if ch in trie.child:
            trie = trie.child[ch]
            min_freq = min(min_freq, trie.freq)
        else:
            min_freq = 0
        
    return min_freq

class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        trie = TrieNode()
        output = []
        
        for op, word in zip(A, B):
            if op:
                output.append(get_freq(trie, word))
            else:
                insert(trie, word)


        return output