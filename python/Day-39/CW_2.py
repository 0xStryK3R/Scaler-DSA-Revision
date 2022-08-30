class Solution:
	# @param A : integer
	# @return a list of strings
    def generate(self, lt, rt, cur_str):
        if len(cur_str)==2*self.A:
            self.ans.append(''.join(cur_str))
            return
        
        if lt<self.A:
            cur_str.append('(')
            self.generate(lt+1, rt, cur_str)
            cur_str.pop()
        
        if rt<lt:
            cur_str.append(')')
            self.generate(lt, rt+1, cur_str)
            cur_str.pop()

    def generateParenthesis(self, A):
        self.A = A
        
        self.ans = []
        self.generate(0, 0, [])

        return self.ans
