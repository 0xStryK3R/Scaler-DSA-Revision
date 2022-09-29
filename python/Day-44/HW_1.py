class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        A = list(A)
        hash_A = {}
        N = len(A)
        for i in range(N):
            A[i] = "".join(sorted(A[i]))
            hash_A.setdefault(A[i], [])
            hash_A[A[i]].append(i + 1)

        return list(
            hash_A.values()
        )  # Dictionary is now inserion ordered in python 3.7+
