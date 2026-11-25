class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n == 0:
            return 0
        dp = [[-1] * n for _ in range(n)]
        def solve(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            ans=solve(i,j-1)+1
            #print(ans)
            for k in range(i,j):
                if s[k]==s[j]:
                    ans=min(ans,solve(k+1,j-1)+solve(i,k))
            dp[i][j]=ans
            return ans
        return solve(0,len(s)-1)
