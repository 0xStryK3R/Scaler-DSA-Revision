class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @return an integer
    def swap(self, i, j):
        self.pos_map[self.B[i]] = j
        self.pos_map[self.B[j]] = i
        self.B[i], self.B[j] =  self.B[j], self.B[i]

    def arrange_pairs(self, pair_idx, swap_count):
        if pair_idx == self.A:
            return swap_count
        
        cur_idx = pair_idx*2
        fa = self.B[cur_idx]
        fb = self.pair_map[fa]
        sa = self.B[cur_idx+1]
        sb = self.pair_map[sa]

        if fb == sa:
            return self.arrange_pairs(pair_idx+1, swap_count)
        else:
            # Matching first element by swapping second
            i = cur_idx+1
            j = self.pos_map[fb]
            self.swap(i, j)
            sec_ele_swap = self.arrange_pairs(pair_idx+1, swap_count+1)
            self.swap(i, j)

            # Matching second element by swapping first
            i = cur_idx
            j = self.pos_map[sa]
            self.swap(i, j)
            first_ele_swap = self.arrange_pairs(pair_idx+1, swap_count+1)
            self.swap(i, j)

            return min(first_ele_swap, sec_ele_swap)            

    def solve(self, A, B, C):
        self.N = len(B)
        pair_map = {}
        for f, s in C:
            pair_map[f] = s
            pair_map[s] = f
        
        pos_map = {}
        for i, val in enumerate(B):
            pos_map[val] = i
        
        self.A = A
        self.B = B
        self.C = C
        self.pair_map = pair_map
        self.pos_map = pos_map

        swap_count = self.arrange_pairs(0, 0)

        return swap_count

