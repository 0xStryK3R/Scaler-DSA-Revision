class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        ans = [0]
        for i in range(A):
            batch = []
            for num in ans[::-1]:
                batch.append(num | 1 << i)
            ans.extend(batch)
        return ans
