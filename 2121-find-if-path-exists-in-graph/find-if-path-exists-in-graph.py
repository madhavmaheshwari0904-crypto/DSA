class Solution(object):
    def validPath(self, n, edges, x, y):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist = [-1] * (n + 1)
        dist[x] = 0
        q = deque([x])

        while q:
            u = q.popleft()
            if u == y:
                return True
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)

        return False