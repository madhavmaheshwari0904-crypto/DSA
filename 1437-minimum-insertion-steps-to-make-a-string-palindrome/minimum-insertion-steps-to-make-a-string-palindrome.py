class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        def solve(i,j,dp):
            if i>j:
                return 0
            if i==j:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==s[j]:
                dp[i][j]=2+solve(i+1,j-1,dp)
            else:
                dp[i][j]=max(solve(i+1,j,dp),solve(i,j-1,dp))
            return dp[i][j]
        dp=[[-1]*(len(s)+1)for _ in range(len(s)+1)]
        ans=solve(0,len(s)-1,dp)
        return len(s)-ans         