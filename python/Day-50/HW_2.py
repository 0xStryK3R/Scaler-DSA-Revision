class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        all_brakets = set(["{", "}", "[", "]", "(", ")", "+", "-", "*", "/"])
        bracket_dict = {"}": "{", "]": "[", ")": "("}
        main_stck = []

        red_bracket = 0

        for c in A:
            rev_bracket = bracket_dict.get(c, False)
            if rev_bracket:
                red_bracket = 1
                while main_stck.pop() != rev_bracket:
                    red_bracket = 0
            elif c in all_brakets:
                main_stck.append(c)

        return red_bracket
