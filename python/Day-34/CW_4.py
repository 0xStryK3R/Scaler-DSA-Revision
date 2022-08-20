class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def getIntersection(self, A, B):
        total_count = 0
        
        total_count += (A*(A-1))>>1
        
        total_count += (B*(B-1))

        total_count += 2*A*B

        return total_count