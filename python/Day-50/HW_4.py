MAX_CHAR = 26


def adjSign(s, i):
    if i == 0:
        return 1
    if s[i - 1] == "-":
        return 0
    return 1


def evaluate(s, v, add):
    stk = []
    stk.append(1)
    n = len(s)
    i = 0
    while i < n:
        if s[i] == "+" or s[i] == "-":
            i += 1
            continue

        if s[i] == "(":
            if adjSign(s, i):
                stk.append(stk[-1])
            else:
                stk.append(1 - stk[-1])

        elif s[i] == ")":
            stk.pop()

        else:
            if stk[-1]:
                if adjSign(s, i):
                    if add == 1:
                        v[ord(s[i]) - 97] += 1
                    else:
                        v[ord(s[i]) - 97] -= 1
                else:
                    if add == 1:
                        v[ord(s[i]) - 97] -= 1
                    else:
                        v[ord(s[i]) - 97] += 1
                # v[ord(s[i]) - 97] += (adjSign(s, i) ? add ? 1 : -1 : add ? -1 : 1);
            else:
                if adjSign(s, i):
                    if add == 1:
                        v[ord(s[i]) - 97] -= 1
                    else:
                        v[ord(s[i]) - 97] += 1
                else:
                    if add == 1:
                        v[ord(s[i]) - 97] += 1
                    else:
                        v[ord(s[i]) - 97] -= 1

        i += 1


def areSame(expr1, expr2):
    v = [0] * MAX_CHAR
    evaluate(expr1, v, 1)
    evaluate(expr2, v, 0)
    for i in range(MAX_CHAR):
        if v[i] != 0:
            return 0
    return 1


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        if areSame(A, B):
            return 1
        return 0
