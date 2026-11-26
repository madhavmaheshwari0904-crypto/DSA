class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n=len(edges)
        vist=[False]*n
        time=1
        ans=-1
        for i in range(n):
            if vist[i]:
                continue
            start=time
            curr=i
            while curr!=-1 and   not vist[curr]:
                vist[curr]=time
                time+=1
                curr=edges[curr]
            if curr != -1 and vist[curr] >= start:
                ans= max(ans, time - vist[curr])
        return ans