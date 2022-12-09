class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        q = []
        front = 0
        ch_set = set()
        repeat_set = set()
        ans = []
        for ch in A:
            if ch in ch_set:
                repeat_set.add(ch)
            ch_set.add(ch)
            q.append(ch)
            ql = len(q)
            while front < ql and q[front] in repeat_set:
                front += 1
            if front == ql:
                ans.append("#")
            else:
                ans.append(q[front])
        return "".join(ans)
