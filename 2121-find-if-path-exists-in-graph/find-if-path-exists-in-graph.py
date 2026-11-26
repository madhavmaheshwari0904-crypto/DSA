class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        #creat adj_list
        adj_list=[]
        for _ in range(n):
            adj_list.append([])
        for l in edges:
            adj_list[l[0]].append(l[1])
            adj_list[l[1]].append(l[0])
        print(adj_list)
        #apply bfs
        visted=[False]*len(adj_list)
        q=deque([source])
        visted[source]=True
        while q:
            u=q.popleft()
            if u==destination:
                return True
            for v in adj_list[u]:
                if not visted[v]:
                    q.append(v)
                    visted[v]=True
        return False