class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        operators = ["+", "-", "*", "/"]

        for ch in A:
            if ch in operators:
                # print(111, ch, stack)
                b = int(stack.pop())
                a = int(stack.pop())
                if ch == "+":
                    c = a + b
                elif ch == "-":
                    c = a - b
                elif ch == "*":
                    c = a * b
                else:
                    c = a // b
                stack.append(c)
            else:
                # print(ch)
                stack.append(ch)

        return stack.pop()
