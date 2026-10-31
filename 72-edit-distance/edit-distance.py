class Solution(object):
    def minDistance(self, s, t):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """n1, n2 = len(word1), len(word2)
        prev = [j for j in range(n2 + 1)]
        curr = [0] * (n2 + 1)
        
        for i in range(1, n1 + 1):
            curr[0] = i
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    insertion = 1 + curr[j - 1]
                    deletion = 1 + prev[j]
                    replacement = 1 + prev[j - 1]
                    curr[j] = min(insertion, deletion, replacement)
            prev = curr[:]
        
        return prev[n2]"""
        def solve(i,j,dp):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if dp[j][i]!=-1:
                return dp[j][i]
            if s[i]==t[j]:
                dp[j][i]=solve(i-1,j-1,dp)
            else: dp[j][i]=1+min(solve(i,j-1,dp),solve(i-1,j,dp),solve(i-1,j-1,dp))
            return dp[j][i]
        dp=[[-1]*len(s)for _ in range(len(t))]
        return solve(len(s)-1,len(t)-1,dp)