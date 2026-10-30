
from heapq import heappop, heappush
class Solution:
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        n=len(heights)
        m=len(heights[0])
        visited = [[float('inf')] * m for _ in range(n)]
        """for i in range(len(heights)):
            for j in range(len(heights[0])):
                visted[i][j]=float('inf')"""
        heap=[(0,0,0)]
        visited[0][0]=0
        dr=[-1,0,1,0]
        dc=[0,-1,0,1]
        while heap:
            r,dis,c=heappop(heap)
            if(r==n-1 and c==m-1):return dis
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if(nr>=0 and nc>=0 and nr<n and nc<m):
                    effort=max(dis,abs(heights[r][c]-heights[nr][nc]))
                    if effort<visited[nr][nc]:
                        visited[nr][nc]=effort
                        heappush(heap,(nr,effort,nc))
        return 0