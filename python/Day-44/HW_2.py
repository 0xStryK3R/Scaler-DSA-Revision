import random

N = 100000
INF = 1 << 46
Hash = {}


def rand46():  # generates 46bit random number
    ret = 0
    ret |= random.randint(0, INF)
    x = random.randint(0, INF)
    ret = ret | (x << 15)
    return ret


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)

        hash_A = {}
        Ps_arr = [0] * (N + 1)

        for i in range(N):
            hash_A[A[i]] = hash_A.get(A[i], rand46())
            Ps_arr[i + 1] = Ps_arr[i] + hash_A[A[i]]

        ans = []
        for l1, r1, l2, r2 in B:
            if Ps_arr[r1 + 1] - Ps_arr[l1] == Ps_arr[r2 + 1] - Ps_arr[l2]:
                ans.append(1)
            else:
                ans.append(0)

        return ans
