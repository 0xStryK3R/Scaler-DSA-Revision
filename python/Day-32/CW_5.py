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
    # @return an integer
    # Divisor Function ==> https://www.youtube.com/watch?v=5ltOfUUb-7U

    def solve(self, A):
        MOD = 10**9 + 7
        ans = 1
        for prime in sieve(A):
            prime_div_count = 0
            num = A
            while num:
                num //= prime
                prime_div_count += num
            ans = (
                ans * ((pow(prime, prime_div_count + 1) - 1) // (prime - 1)) % MOD
            ) % MOD

        return ans
