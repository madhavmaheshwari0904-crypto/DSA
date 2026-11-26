class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # center vertice is in which adjectent matrix of a particular row sum==number vertics-1
        maxi=-1
        for i in edges:
            m=max(i)
            maxi=max(maxi,m)
        #print(maxi)
        adj_mat=[[]for _ in range(maxi+1)]
        #print(adj_mat)
        for a,b in edges:
            adj_mat[a].append(b)
            adj_mat[b].append(a)
        #print(adj_mat)
        for j in range(1, maxi + 1):
            # Use len() to count neighbors, not sum()
            if len(adj_mat[j]) == maxi - 1:
                return j