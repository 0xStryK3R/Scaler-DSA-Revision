class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        pos_num = []
        neg_num = []
        for num in A:
            if num < 0:
                neg_num.append(num)
            else:
                pos_num.append(num)

        neg_num = neg_num[::-1]
        pos_num = pos_num[::-1]

        i = 0
        while neg_num and pos_num:
            if i & 1:
                ans.append(pos_num.pop())
            else:
                ans.append(neg_num.pop())
            i += 1

        if neg_num:
            ans.extend(neg_num[::-1])
        else:
            ans.extend(pos_num[::-1])

        return ans
