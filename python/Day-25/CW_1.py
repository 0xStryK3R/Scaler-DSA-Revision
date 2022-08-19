class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        if len(A) < 1:
            return 0
        if not A[0]:
            A = [1] + A
        flip_cnt = 0
        current_state = 1

        for bulb in A:
            if bulb != current_state:
                flip_cnt += 1
                current_state = bulb

        return flip_cnt
