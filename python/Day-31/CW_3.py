class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, A, B):
        B, A = sorted([abs(A), abs(B)])
        if B == 0:
            return A
        return self.gcd(B, A % B)

    def solve(self, A):
        N = len(A)

        # Creating prefix and postfix gcd arrays
        prefix = [0] * N
        suffix = [0] * N

        prefix[0] = A[0]
        suffix[-1] = A[-1]

        for i in range(1, N):
            prefix[i] = self.gcd(prefix[i - 1], A[i])

        for i in range(N - 2, -1, -1):
            suffix[i] = self.gcd(suffix[i + 1], A[i])

        # For Max GCD without a single element, first skipping first and last element and checking
        ans = max(prefix[-2], suffix[1])

        # Then, rolling over the entire list of elements by taking gcd of 'gcd of all elements
        # to its left' and `gcd of all elemnts to its right` - hence, skipping the current element itself.
        for i in range(1, N - 1):
            ans = max(ans, self.gcd(prefix[i - 1], suffix[i + 1]))

        return ans
