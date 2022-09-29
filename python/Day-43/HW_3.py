class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def minWindow(self, A, B):
        counter = {}
        total_ch = len(B)
        
        for ch in B:
            counter[ch] = counter.get(ch, 0) + 1
        
        l = -1
        r = 0
        N = min_len = len(A)
        best_l = best_r = -1
        
        while(r<N):
            if A[r] in counter:
                if l<0:
                    l = r
                    best_l = l
                    best_r = r
                    
                counter[A[r]] -= 1
                if counter[A[r]]>-1:
                    total_ch -= 1
                    
                if not total_ch:
                    if counter[A[l]]<0:
                        while(A[l] not in counter or counter[A[l]]<0):
                            if A[l] in counter:
                                counter[A[l]] += 1
                            l += 1

                    if r-l+1<min_len:
                        min_len = r-l+1
                        best_l = l
                        best_r = r
            r += 1
        
        if total_ch:
            return ''
        
        return A[best_l:best_r+1]