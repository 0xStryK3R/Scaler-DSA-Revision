n = 4
a, b, c = 2, 3, 4


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        pointer_a = 0
        pointer_b = 0
        pointer_c = 0

        ans = max(A[pointer_a], B[pointer_b], C[pointer_c]) - min(
            A[pointer_a], B[pointer_b], C[pointer_c]
        )

        while True:
            if A[pointer_a] > B[pointer_b] and A[pointer_a] > C[pointer_c]:
                if pointer_c < len(C) - 1 and B[pointer_b] > C[pointer_c]:
                    pointer_c += 1
                elif pointer_b < len(B) - 1:
                    pointer_b += 1
                else:
                    break
            elif B[pointer_b] > C[pointer_c]:
                if pointer_c < len(C) - 1 and A[pointer_a] > C[pointer_c]:
                    pointer_c += 1
                elif pointer_a < len(A) - 1:
                    pointer_a += 1
                else:
                    break
            else:
                if pointer_b < len(B) - 1 and A[pointer_a] > B[pointer_b]:
                    pointer_b += 1
                elif pointer_a < len(A) - 1:
                    pointer_a += 1
                else:
                    break

            ans = min(
                ans,
                max(A[pointer_a], B[pointer_b], C[pointer_c])
                - min(A[pointer_a], B[pointer_b], C[pointer_c]),
            )

        ans = min(
            ans,
            max(A[pointer_a], B[pointer_b], C[pointer_c])
            - min(A[pointer_a], B[pointer_b], C[pointer_c]),
        )

        return ans
