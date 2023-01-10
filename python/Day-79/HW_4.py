from heapq import heappush, heappop
g = []
maxn = 1000000000
visited = []

def dijkstra(A, f, t, timed):
    global g, visited, maxn
    dist = [maxn] * (A + 1)
    dist[f] = 0
    pq = []
    heappush(pq, [0, f])
    while(len(pq) != 0):
        temp = heappop(pq)
        v = temp[1]
        if(visited[v] == timed):
            continue
        visited[v] = timed
        for node in g[v]:
            w = node[0]
            u = node[1]
            if(v == f and u == t):
                continue
            elif(v == t and u == f):
                continue
            if(dist[v] + w < dist[u]):
                dist[u] = dist[v] + w
                heappush(pq, [dist[u], u])
    if(dist[t] == maxn):
        return -1
    return dist[t]


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        global g, visited, maxn
        g = [[] for i in range(A + 1)]
        for i in B:
            g[i[0]].append((i[2], i[1]))
            g[i[1]].append((i[2], i[0]))
        visited = [0] * (A + 1)
        ans = maxn
        timed = 0
        for i in B:
            timed += 1
            res = dijkstra(A, i[0], i[1], timed)
            if(res == -1):
                continue
            ans = min(ans, res + i[2])
        if(ans == maxn):
            ans = -1
        return ans