class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer#Sieve Algo
    def find_all_primes(self, N):
        prime = {i: True for i in range(N + 1)}
        prime[0] = prime[1] = False
        i = 2
        while i * i <= N:
            j = i
            if prime.get(i, True):
                while j * i <= N:
                    prime[i * j] = False
                    j += 1
            i += 1
        return prime  # list(filter(lambda x: prime[x], range(N+1)))

    def solve(self, A, B):
        prime_list = self.find_all_primes(B)
        ans = 0
        for i in A:
            if prime_list.get(i, False) and B % i == 0:
                ans += 1
        return ans
