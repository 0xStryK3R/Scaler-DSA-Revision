class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        count = 0
        hash_A = {}
        for c in A:
            hash_A[c] = hash_A.get(c, 0) + 1
        break_point = -1
        hash_B = {}
        for i in range(len(B)):
            if B[i] in hash_A:
                hash_B[B[i]] = hash_B.get(B[i], 0) + 1
                if i - N > break_point and B[i - N] in hash_A and B[i - N] in hash_B:
                    hash_B[B[i - N]] = hash_B.get(B[i - N], 0) - 1

                if hash_A == hash_B:
                    count += 1
            else:
                hash_B = {}
                break_point = i

        return count
