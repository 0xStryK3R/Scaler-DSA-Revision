# Check sum for each Row-wise Sub-arr and similarly for each column-wise sub-arr.
# If sum is more then target, flip all elements in current sub-arr one by one
# and recheck for entire grid.

grid = [[]]
allowed = -1
NEGINF = -1e9


def rec(ops):
    global grid
    global allowed
    if ops == -1:
        return 0

    ret = 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            sm = 0
            for k in range(j, len(grid[0])):
                sm += grid[i][k]
                if sm > allowed:
                    ret = 0
                    for l in range(j, k + 1):
                        grid[i][l] = -grid[i][l]
                        ret |= rec(ops - 1)
                        grid[i][l] = -grid[i][l]

                    return ret

    for j in range(len(grid[0])):
        for i in range(len(grid)):
            sm = 0
            for k in range(i, len(grid)):
                sm += grid[k][j]
                if sm > allowed:
                    ret = 0
                    for l in range(i, k + 1):
                        grid[l][j] = -grid[l][j]
                        ret |= rec(ops - 1)
                        grid[l][j] = -grid[l][j]
                    return ret

    return ret


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        global grid, allowed
        grid = B
        allowed = C
        return rec(A)
