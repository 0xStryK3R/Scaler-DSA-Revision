class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        me = None
        cnt = 0

        for num in A:
            if not me:
                me = num
                cnt += 1
            else:
                if num == me:
                    cnt += 1
                else:
                    cnt -= 1
            if cnt == 0:
                me = None

        return me
