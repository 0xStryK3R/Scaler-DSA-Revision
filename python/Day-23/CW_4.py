class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        ans = [1]
        ptr_A = ptr_B = ptr_C = 0

        ans_set = set(ans)

        while len(ans) <= D:
            next_num_A = ans[ptr_A] * A
            while next_num_A in ans_set:
                ptr_A += 1
                next_num_A = ans[ptr_A] * A
            next_num_B = ans[ptr_B] * B
            while next_num_B in ans_set:
                ptr_B += 1
                next_num_B = ans[ptr_B] * B
            next_num_C = ans[ptr_C] * C
            while next_num_C in ans_set:
                ptr_C += 1
                next_num_C = ans[ptr_C] * C

            if next_num_A < next_num_B:
                if next_num_A < next_num_C:
                    ans.append(next_num_A)
                    ans_set.add(next_num_A)
                    ptr_A += 1
                else:
                    ans.append(next_num_C)
                    ans_set.add(next_num_C)
                    ptr_C += 1
            else:
                if next_num_B < next_num_C:
                    ans.append(next_num_B)
                    ans_set.add(next_num_B)
                    ptr_B += 1
                else:
                    ans.append(next_num_C)
                    ans_set.add(next_num_C)
                    ptr_C += 1

        return ans[1:]
