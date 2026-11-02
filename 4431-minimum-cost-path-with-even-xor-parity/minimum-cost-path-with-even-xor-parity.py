class Solution:
    def minActivationCost(self, edges: list[list[int]], A: list[int]) -> int:
        mn = [inf] * len(A)
        res = inf
        for i, j, c in edges:
            vi = A[i].bit_count() & 1
            vj = A[j].bit_count() & 1
            if vi == vj:
                res = min(res, c)
            else:
                zero = i if vj else j
                res = min(res, mn[zero] + c)
                mn[zero] = min(mn[zero], c)
        return res if res < inf else -1