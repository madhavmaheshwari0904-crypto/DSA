class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        """cuts.append(0)
        cuts.append(n)
        cuts.sort()
        c=len(cuts)-2
        dp = [[0] * (c + 2) for _ in range(c + 2)]
        for i in range(c,0,-1):
            for j in range(i,c+1):
                mimi=float('inf')
                for k in range(i,j+1):
                    cost=cuts[j+1]-cuts[i-1]+dp[i][k-1]+dp[k+1][j]
                    mimi=min(mimi,cost)
                dp[i][j]=mimi
        return [1][c]"""
        cuts.append(0)
        cuts.append(n)
        cuts.sort()

        c = len(cuts) - 2
        dp = [[0] * (c + 2) for _ in range(c + 2)]

        for i in range(c, 0, -1):
            for j in range(i, c + 1):
                mimi = float("inf")
                for k in range(i, j + 1):
                    # Subtraction gives the segment length
                    cost = (
                        (cuts[j + 1] - cuts[i - 1])
                        + dp[i][k - 1]
                        + dp[k + 1][j]
                    )
                    mimi = min(mimi, cost)
                dp[i][j] = mimi

        return dp[1][c]
