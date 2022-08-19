class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        row_val_set = set()
        duplicate_rows = []
        for i in range(len(A)):
            row_val = "".join(list(map(str, A[i])))
            if row_val in row_val_set:
                duplicate_rows.append(i + 1)
            row_val_set.add(row_val)

        return duplicate_rows
