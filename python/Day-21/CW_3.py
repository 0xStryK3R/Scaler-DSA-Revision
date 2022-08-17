class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        Prefix_S_arr = [0]
        for num in A:
            Prefix_S_arr.append(Prefix_S_arr[-1] + num)
        
        Postix_S_arr = [0]
        for num in A[::-1]:
            Postix_S_arr.append(Postix_S_arr[-1] + num)
        
        Postix_S_arr = Postix_S_arr[::-1]

        for i in range(len(A)):
            if Prefix_S_arr[i] == Postix_S_arr[i+1]:
                return i
        
        return -1

