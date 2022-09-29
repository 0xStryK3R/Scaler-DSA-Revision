class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
        A.sort()
        N = len(A)
        closest_ans = sum(A[:3])
        for i in range(N):
            a = A[i]
            l = i + 1
            r = N - 1

            while(l<r):
                cur_sum = a + A[l] + A[r]
                if cur_sum == B:
                    return B
                if abs(B - cur_sum) < abs(B - closest_ans):
                    closest_ans = cur_sum
                if cur_sum < B:
                    l += 1
                else:
                    r -= 1    
        return closest_ans
