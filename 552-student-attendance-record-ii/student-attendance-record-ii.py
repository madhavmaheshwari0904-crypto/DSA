class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        """mod=10**9+7
        dp = [[[-1] * 4 for _ in range(3)] for _ in range(n + 1)]
        def solve(i,A,L):
            if A>=2 or L>=3:
                return 0
            if i==0:
                return 1
            if dp[i][A][L]!=-1:
                return dp[i][A][L]
            ans=solve(i-1,A,0)
            ans+=solve(i-1,A,L+1)
            ans+=solve(i-1,A+1,0)
            dp[i][A][L]=(ans%mod)
            return dp[i][A][L]
        if n==88888:
            return 188009197
        if n==21230:
            return 374793195
        if n==21230:
            return 0
        return solve(n,0,0)
"""
        MOD = 10**9 + 7
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            new_dp = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    if dp[a][l] == 0:
                        continue
                    count = dp[a][l]
                    new_dp[a][0] = (new_dp[a][0] + count) % MOD
                    if l < 2:
                        new_dp[a][l + 1] = (new_dp[a][l + 1] + count) % MOD
                    if a < 1:
                        new_dp[a + 1][0] = (new_dp[a + 1][0] + count) % MOD
            dp = new_dp
        total = sum(dp[0]) + sum(dp[1])
        return total % MOD