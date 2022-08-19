class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A == 0:
            return [1]

        prev_row = [1]

        for a in range(1, A + 1):
            cur_row = [1]
            for i in range(1, a):
                cur_row.append(prev_row[i] + prev_row[i - 1])
            cur_row.append(1)
            prev_row = cur_row

        return cur_row
