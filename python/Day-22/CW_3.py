class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        d = C - B

        div_list = []

        i = 1

        while i * i <= d:
            if d % i == 0:
                if i < A:
                    div_list.append(d // i)
                if d // i < A and i != d // i:
                    div_list.append(i)
            i += 1

        div_list.sort(reverse=True)

        for div in div_list:
            if C // div >= A:
                break

        ans = [C]

        for i in range(A - 1):
            if ans[0] - div > 0:
                ans = [ans[0] - div] + ans
            else:
                ans.append(ans[-1] + div)

        return ans
