class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v, w in times:
            adj[u - 1].append((v - 1, w))
        k -= 1
        dis=[float('inf')]*n
        vis=[False]*n
        dis[k]=0
        l=[]
        l.append((0,k))
        while l:
            time,node=heapq.heappop(l)
            if time>dis[node]:
                continue
            for v,w in adj[node]:
                if w+time<dis[v]:
                    dis[v]=w+time
                    heapq.heappush(l,(dis[v],v))
        ans=max(dis)
        return -1 if ans==float('inf') else ans