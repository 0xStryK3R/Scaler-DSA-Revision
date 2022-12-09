def postifixize(stack):
    priority_mat = {"^": 2, "*": 1, "/": 1, "+": 0, "-": 0}

    symbols = list(priority_mat.keys())
    main_stack = []
    symbol_stack = []

    for ch in stack:
        if ch in symbols:
            while symbol_stack and priority_mat[symbol_stack[-1]] >= priority_mat[ch]:
                s = symbol_stack.pop()
                r = main_stack.pop()
                l = main_stack.pop()
                main_stack.append(l + r + s)
            symbol_stack.append(ch)
        else:
            main_stack.append(ch)

    while symbol_stack:
        main_stack.append(symbol_stack.pop())

    return "".join(main_stack)


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        N = len(A)
        stack = []

        i = 0
        while i < N:
            ch = A[i]
            if ch == "(":
                bracket_cnt = 1
                i += 1
                tmp_str = ""
                while i < N:
                    if A[i] == "(":
                        bracket_cnt += 1
                    elif A[i] == ")":
                        bracket_cnt -= 1
                        if not bracket_cnt:
                            break
                    tmp_str += A[i]
                    i += 1
                ch = self.solve(tmp_str)

            stack.append(ch)
            i += 1

        return postifixize(stack)
