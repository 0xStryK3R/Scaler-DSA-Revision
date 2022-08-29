class Solution:
    # @param A : list of list of chars
    def generate(self, row_map, col_map, box_map, cur_idx):
        if cur_idx == 81:
            self.ans = ["".join(row) for row in self.A]
            # print(self.ans)
            return

        i, j = cur_idx // 9, cur_idx % 9

        if self.A[i][j] == ".":
            for a in range(1, 10):
                if (
                    row_map[i] & (1 << a)
                    or col_map[j] & (1 << a)
                    or box_map[i // 3][j // 3] & (1 << a)
                ):
                    continue

                row_map[i] ^= 1 << a
                col_map[j] ^= 1 << a
                box_map[i // 3][j // 3] ^= 1 << a

                self.A[i][j] = str(a)

                self.generate(row_map, col_map, box_map, cur_idx + 1)

                self.A[i][j] = "."

                row_map[i] ^= 1 << a
                col_map[j] ^= 1 << a
                box_map[i // 3][j // 3] ^= 1 << a
        else:
            self.generate(row_map, col_map, box_map, cur_idx + 1)

    def solveSudoku(self, A):
        self.A = A
        self.ans = []

        row_map = [0] * 9
        col_map = [0] * 9
        box_map = [[0] * 3 for i in range(3)]

        for i in range(9):
            for j in range(9):
                a = A[i][j]
                if a == ".":
                    continue
                a = int(a)
                row_map[i] ^= 1 << a
                col_map[j] ^= 1 << a
                box_map[i // 3][j // 3] ^= 1 << a

        self.generate(row_map, col_map, box_map, 0)

        for i, row in enumerate(self.ans):
            A[i] = row

        return
