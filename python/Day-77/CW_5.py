class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dir_map = {}
        for i, v in enumerate(A[1:]):
            dir_map.setdefault(v, set())
            dir_map[v].add(i + 2)

        queue = [C]

        while queue:
            if B in queue:
                return 1
            next_queue = []
            for node in queue:
                next_queue.extend(list(dir_map.get(node, [])))

            queue = next_queue

        return 0
