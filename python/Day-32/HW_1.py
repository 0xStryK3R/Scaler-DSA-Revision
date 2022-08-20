# Sieve Algo
def sieve(A):
    N = A
    prime = [True] * (N + 1)
    prime[0] = prime[1] = False
    i = 2
    while i * i <= N:
        j = i
        if prime[i]:
            while j * i <= N:
                prime[i * j] = False
                j += 1
        i += 1

    return list(filter(lambda x: prime[x], range(N + 1)))


class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        primes = sieve(A)

        l = 0
        r = len(primes) - 1
        while l <= r:
            pair_sum = primes[l] + primes[r]
            if pair_sum > A:
                r -= 1
            elif pair_sum < A:
                l += 1
            else:
                return [primes[l], primes[r]]
