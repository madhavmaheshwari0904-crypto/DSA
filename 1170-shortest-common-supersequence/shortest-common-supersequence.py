class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def solve(i,j,dp):
            ans=""
            while i>0 and j>0:
                if str1[i-1]==str2[j-1]:
                    ans+=str1[i-1]
                    i-=1
                    j-=1
                elif dp[i-1][j]>dp[i][j-1]:
                    ans+=str1[i-1]
                    i-=1
                else:
                    ans+=str2[j-1]
                    j-=1
            while i>0:
                ans+=str1[i-1]
                i-=1
            while j>0:
                ans+=str2[j-1]
                j-=1
            return ans[::-1]
                
        n1=len(str1)
        n2=len(str2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    
        return solve(n1,n2,dp)