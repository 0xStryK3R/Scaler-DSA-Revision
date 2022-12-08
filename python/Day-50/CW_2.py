class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        main_stack = [A.pop()]
        rev_stack = []

        while A:
            nxt = A.pop()
            while main_stack and nxt < main_stack[-1]:
                rev_stack.append(main_stack.pop())
            main_stack.append(nxt)
            while rev_stack:
                main_stack.append(rev_stack.pop())

        return main_stack
