class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        bracket_dict = {"}": "{", "]": "[", ")": "("}
        main_stck = []

        for c in A:
            rev_bracket = bracket_dict.get(c, False)
            if rev_bracket:
                if not main_stck or main_stck.pop() != rev_bracket:
                    return 0
            else:
                main_stck.append(c)
        if main_stck:
            return 0
        return 1
