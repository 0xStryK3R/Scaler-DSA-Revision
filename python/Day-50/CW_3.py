class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        main_stack = []
        rev_stack = []
        freq_map = {}
        res = []

        for op, x in A:
            if op == 1:
                freq_map[x] = freq_map.get(x, 0) + 1
                cur_freq = freq_map[x]
                while main_stack and cur_freq < main_stack[-1][-1]:
                    rev_stack.append(main_stack.pop())
                main_stack.append((x, cur_freq))
                while rev_stack:
                    main_stack.append(rev_stack.pop())
                res.append(-1)
            else:
                x, _ = main_stack.pop()
                freq_map[x] = freq_map.get(x, 0) - 1
                res.append(x)
        return res
