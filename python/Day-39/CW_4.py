class Solution:
    # @param A : integer
    # @return a list of list of strings
    def toggle_queen(self, i, j, val="Q"):
        self.col_map[j] ^= 1
        self.lt_dia_map[i - j + self.A - 1] ^= 1
        self.rt_dia_map[i + j] ^= 1

    def generate(self, row_idx, cur_board):
        if row_idx == self.A:
            # print(cur_board)
            self.ans.append(["".join(row) for row in cur_board])
            return

        cur_row = ["."] * self.A

        for col_idx in range(self.A):
            if (
                self.col_map[col_idx]
                or self.lt_dia_map[row_idx - col_idx + self.A - 1]
                or self.rt_dia_map[row_idx + col_idx]
            ):
                continue
            else:
                cur_row[col_idx] = "Q"
                cur_board.append(cur_row)
                self.toggle_queen(row_idx, col_idx)

                self.generate(row_idx + 1, cur_board)

                self.toggle_queen(row_idx, col_idx, ".")
                cur_board.pop()
                cur_row[col_idx] = "."

    def solveNQueens(self, A):
        self.A = A
        self.col_map = [0] * A
        self.lt_dia_map = [0] * (2 * A - 1)
        self.rt_dia_map = [0] * (2 * A - 1)

        self.ans = []
        self.generate(0, [])

        return self.ans
