class Solution:
    # @param A : list of integers
    # @return an integer
    def merge(self, A, start, mid, end):
        m = 10**9 + 7
        count = 0
        i = start
        j = mid
        sorted_subarr = []
        while i < mid and j < end:
            if A[i] <= A[j]:
                sorted_subarr.append(A[i])
                count += j - mid
                i += 1
            else:
                sorted_subarr.append(A[j])
                j += 1
        if i < mid:
            sorted_subarr.extend(A[i:mid])
            count += (end - mid) * (mid - i)
        elif j < end:
            sorted_subarr.extend(A[j:end])
        for i in range(start, end):
            A[i] = sorted_subarr[i - start]
        return count

    def solve(self, A, start=0, end=None):
        m = 10**9 + 7
        if end == None:
            end = len(A)
        count = 0
        if start + 1 == end:
            return 0
        mid = (start + end) >> 1
        count += self.solve(A, start, mid)
        count += self.solve(A, mid, end)
        count += self.merge(A, start, mid, end)
        return count % m
