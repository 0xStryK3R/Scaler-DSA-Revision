class Solution:
	# @param A : list of integers
	# @return a list of integers
    def prevSmaller(self, A):
        stack = []
        ans = []

        for num in A:
            while(stack and stack[-1] >= num):
                stack.pop()
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
            stack.append(num)
        
        return ans