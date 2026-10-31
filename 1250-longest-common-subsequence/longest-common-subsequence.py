class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def solve(text1,i,text2,j,dp):
            ans=0
            if i == 0 or j == 0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if(text1[i-1]==text2[j-1]):
                dp[i][j]=1+solve(text1[:i-1],i-1,text2[:j-1],j-1,dp)
            else:
                dp[i][j]=max(solve(text1[:i-1],i-1,text2,j,dp),solve(text1,i,text2[:j-1],j-1,dp))
            return dp[i][j]
        n=len(text1)
        m=len(text2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        return solve(text1,n,text2,m,dp)