class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        n = len(A)
        left = 0
        right = 0
        zerosInWindow = 0
        if A[right] == 0:
            zerosInWindow += 1
        bestLeft = 0
        bestRight = 0

        while right < n:
            if zerosInWindow <= B:
                right += 1
                if right < n and A[right] == 0:
                    zerosInWindow += 1
            if zerosInWindow > B:
                if A[left] == 0:
                    zerosInWindow -= 1
                left += 1

            if right >= n:
                if n - 1 - left > bestRight - bestLeft:
                    bestLeft = left
                    bestRight = n - 1
            elif right - left > bestRight - bestLeft:
                bestLeft = left
                bestRight = right
        if bestRight > n - 1:
            bestRight = n - 1
        ans = [i for i in range(bestLeft, bestRight + 1)]
        return ans
