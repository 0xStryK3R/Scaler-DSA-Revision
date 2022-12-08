class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        odd = ""
        even = ""
        for c in A:
            if ord(c) & 1:
                odd += c
            else:
                even += c

        odd = sorted(odd)
        even = sorted(even)

        if (
            abs(ord(odd[-1]) - ord(even[0])) != 1
            or abs(ord(odd[0]) - ord(even[-1])) != 1
        ):
            return 1
        return 0
