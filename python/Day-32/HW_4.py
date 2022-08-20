class Solution:
    # @param A : list of integers
    # @return an integer
    # Sieve Algo
    def prime_factors(self, A):
        N = A
        prime_factors = [[] for i in range((N + 1))]
        i = 2
        while i <= N:
            j = 2
            while j * i <= N:
                if not prime_factors[i]:
                    prime_factors[i * j].append(i)
                j += 1
            if not prime_factors[i]:
                prime_factors[i].append(i)
            i += 1

        return {i: list(set(j)) for i, j in enumerate(prime_factors)}

    def solve(self, A):
        prime_map = self.prime_factors(max(A))
        distinct_prime_div = set()

        for num in A:
            distinct_prime_div.update(prime_map[num])

        return len(distinct_prime_div)
