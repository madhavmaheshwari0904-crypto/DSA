from collections import deque
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]
        m=len(grid)
        n=len(grid[0])
        dq=[(0,0,k,0)]
        if k>=n+m-2:
            return n+m-2
        vis=set([(0,0,k)])
        while dq:
            i,j,rem,step=dq[0]
            dq.pop(0)
            if i == m - 1 and j == n - 1:
                return step
            for l in range(4):
                ni=i+dx[l]
                nj=j+dy[l]
                if 0 <= ni < m and 0 <= nj < n:
                    new_k = rem - grid[ni][nj]
                    if new_k>=0 and (ni,nj,new_k) not in vis:
                        vis.add((ni,nj,new_k))
                        dq.append((ni,nj,new_k,step+1))
        return -1