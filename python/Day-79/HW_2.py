import sys
sys.setrecursionlimit(10**6)
g = [[]]
visit = []
mark = []

def dfs(u):
    global g, visit
    visit[u] = 1
    for i in range(len(g[u])):
        if(visit[g[u][i]] == 0):
            dfs(g[u][i])

# Returns true if all vertices are strongly connected i.e. can be made as loop


def isConnected(s):
    global g, mark, visit
    # Initialize all vertices as not visited
    visit = [0] * 26

    # perform a dfs from s
    dfs(s)

    # now loop through all characters
    for i in range(26):
        #  I character is marked (i.e. it was first or last character of some string) then it should be visited in last dfs (as for looping, graph
        #    should be strongly connected)
        if (mark[i] == 1 and visit[i] == 0):
            return 0

    # If we reach that means graph is connected
    return 1


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        # Create an empty graph
        global g, mark, visit
        g = [[]for i in range(26)]
        N = len(A)
        # Initialize all vertices as not marked
        mark = [0] * 26

        # Initialize indegree and outdegree of every vertex as 0.
        indeg = [0] * 26
        outdeg = [0] * 26

        # Process all strings one by one
        for i in range(N):
            # Find first and last characters
            f = ord(A[i][0]) - 97
            l = ord(A[i][len(A[i]) - 1]) - 97

            # Mark the characters
            mark[f] = 1
            mark[l] = 1

            # increase indegree and outdegree count
            indeg[l] += 1
            outdeg[f] += 1

            # Add an edge in graph
            g[f].append(l)

        # If for any character indegree is not equal to outdegree then ordering is not possible
        for i in range(26):
            if (indeg[i] != outdeg[i]):
                return 0
        return isConnected(ord(A[0][0]) - 97)