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

def check_dictionary(trie, word, idx=0, flg=True):
    #print(word, idx, flg)
    if idx==len(word):
        return trie.is_end and not flg
    cur_chr = word[idx]
    for ch, trie_child in trie.child.items():
        if flg or ch==cur_chr:
            if check_dictionary(trie_child, word, idx+1, flg and ch==cur_chr):
                return True
    return False

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):

        trie = create_trie(A)
        
        return ''.join([str(int(check_dictionary(trie, word))) for word in B])