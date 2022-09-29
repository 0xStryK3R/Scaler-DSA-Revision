def merge(a, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = a[start + i]
    for j in range(n2):
        R[j] = a[mid + 1 + j]
    i = 0
    j = 0
    for k in range(start, end + 1):
        if j >= n2 or (i < n1 and L[i] <= R[j]):
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1


def mergesort_and_count(a, start, end):
    if start < end:
        mid = (start + end) // 2
        count = mergesort_and_count(a, start, mid) + mergesort_and_count(
            a, mid + 1, end
        )
        j = mid + 1
        for i in range(start, mid + 1):
            while j <= end and a[i] > a[j] * 2:
                j += 1
            count += j - (mid + 1)
        merge(a, start, mid, end)
        return count
    else:
        return 0


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        return mergesort_and_count(A, 0, n - 1)
