class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        left_arr = [1]
        prev = A[0]
        for cur in A[1:]:
            if cur > prev:
                left_arr.append(left_arr[-1] + 1)
            else:
                left_arr.append(1)
            prev = cur

        right_arr = [1]
        for cur in A[::-1][1:]:
            if cur > prev:
                right_arr.append(right_arr[-1] + 1)
            else:
                right_arr.append(1)
            prev = cur

        right_arr.reverse()

        answer = 0
        for i in range(len(left_arr)):
            answer += max(left_arr[i], right_arr[i])

        return answer
