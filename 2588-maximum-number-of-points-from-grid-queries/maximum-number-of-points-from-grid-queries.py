import heapq
from bisect import bisect_left
class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        def binary(arr,x):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        v = {(0, 0)}
        order = []

        while heap:
            curr, i, j = heapq.heappop(heap)
            order.append(curr)
            for x, y in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and (x, y) not in v:
                    v.add((x, y))
                    heapq.heappush(heap, (grid[x][y], x, y))
        #print(order)
        maxYet = -1
        for i in range(len(order)):
            maxYet = max(maxYet, order[i])
            order[i] = maxYet
        #print(order)
        ans=[]
        for i in queries:
            e=binary(order,i)
            ans.append(e)
        return ans