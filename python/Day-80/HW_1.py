def upper_bound_bs(arr, val):
    l = 0
    r = len(arr) - 1
    ans = -1
    while(l<=r):
        mid = (l+r)>>1
        if arr[mid] >= val:
            ans = arr[mid]
            r = mid - 1
        else:
            l = mid + 1            

    return ans

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F):
        adj_map = {i:set() for i in range(1, A+1)}

        for u, v in zip(B, C):
            adj_map[u].add(v)
            adj_map[v].add(u)
        
        level_map = {0:[1]}
        vis = set([1])
        cur_level = 1

        while(len(vis)<A):
            next_level = set()
            for node in level_map[cur_level-1]:
                for child_node in adj_map[node]:
                    if child_node in vis:
                        continue
                    next_level.add(child_node)
                    vis.add(child_node)
            if not next_level:
                break

            level_map[cur_level] = sorted(list(next_level))
            cur_level += 1
        
        for k in level_map.keys():
            level_map[k] = sorted([D[v-1] for v in level_map[k]])
        
        max_depth = len(level_map)
        output = []

        for l, x in zip(E, F):
            l %= max_depth
            output.append(upper_bound_bs(level_map[l], x))
        
        return output

