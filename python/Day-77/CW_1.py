class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        dir_map = {}

        for u, v in B:
            dir_map.setdefault(u, set())
            dir_map[u].add(v)

        queue = [1]

        while queue:
            if A in queue:
                return 1
            next_queue = []
            for node in queue:
                next_queue.extend(list(dir_map.get(node, [])))

            queue = next_queue

        return 0
