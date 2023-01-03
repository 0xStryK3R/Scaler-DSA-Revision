class Solution:
    def isScramble(self, A, B):
        dpMap = dict()

        def helper(i1, i2, l):
            key = (i1, i2, l)
            if key not in dpMap:
                dpMap[key] = l == 0
                if l == 1:
                    dpMap[key] = A[i1] == B[i2]
                else:
                    for ind in range(1, l):
                        if any([
                            helper(i1, i2, ind) and helper(
                                i1+ind, i2+ind, l-ind),
                            helper(i1, i2+l-ind,
                                   ind) and helper(i1+ind, i2, l-ind)
                        ]):
                            dpMap[key] = True
                            break
            return dpMap[key]
        return int(helper(0, 0, len(A)))