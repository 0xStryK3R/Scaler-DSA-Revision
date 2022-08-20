class Solution:
    # @param A : list of integers
    # @return an integer
    def find_all_primes(self, N):
        prime = [True]*(N+1)
        prime[0] = prime[1] = False
        i = 2
        while (i*i<=N):
            j = i
            if prime[i]:
                while(j*i<=N):
                   prime[i*j] = False
                   j += 1
            i += 1
        return list(filter(lambda x: prime[x], range(N+1)))
        
    def solve(self, A):
        m = 10**9 + 7
        max_A = max(A)
        
        # Get All unique prime numbers upto Max of A
        prime_list = self.find_all_primes(max_A)
        
        # Create a map of each number untill Max of A and largest 
        # prime factor less then or equal to it
        prime_bucket = {i: 0 for i in prime_list}
        prime_bucket[1] = 1
        i = 0
        for num in range(2, max_A+1):
            if not (i == len(prime_list) - 1 or num < prime_list[i+1]):
                i += 1
            prime_bucket[num] = prime_list[i]
        
        # Create map of prime numbers and count of numbers from A,
        # where it is largest prime number just equal or lesser then
        reverse_prime_bucket = {}
        for num in A:
            if num == 1:
                continue
            reverse_prime_bucket.setdefault(prime_bucket[num], 0)
            reverse_prime_bucket[prime_bucket[num]] += 1
        
        # Since for given n, n! will have unique prime factors upto 
        # largest prime factor of n, using previous map to calculate 
        # all possible subsequences.
        ans = 0        
        for _, val in reverse_prime_bucket.items():
            ans = (ans + (2**val)%m - 1)%m
        
        return ans