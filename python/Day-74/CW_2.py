class Node:
    def __init__(self, i, w):
        self.items = i
        self.weight = w

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        requiredSum = sum(A)//2
        dp = [[Node(0,0) for j in range(0, requiredSum+1)]for i in range(0, n+1)]

        for i in range(1, n+1):
            for j in range(1, requiredSum+1):
                prev_items = dp[i-1][j].items
                prev_weight = dp[i-1][j].weight

                if j-A[i-1] >= 0:
                    curr_weight = dp[i-1][j-A[i-1]].weight + A[i-1]
                    curr_items = dp[i-1][j-A[i-1]].items + 1

                    if (curr_weight>prev_weight) or ((curr_weight==prev_weight) and (curr_items<prev_items)):
                        dp[i][j] = Node(curr_items, curr_weight)
                    else:
                        dp[i][j] = dp[i-1][j]

                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][requiredSum].items;