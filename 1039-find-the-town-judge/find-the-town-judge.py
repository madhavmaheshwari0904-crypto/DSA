class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        adj_mat = [[0] * n for _ in range(n)]
        for a, b in trust:
            adj_mat[a - 1][b - 1] = 1
            
        for i in range(n):
            row_sum = sum(adj_mat[i])                          
            col_sum = sum(adj_mat[row][i] for row in range(n)) 
            if row_sum == 0 and col_sum == n - 1:
                return i + 1
                
        return -1