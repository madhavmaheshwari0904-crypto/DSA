class Solution(object):
    mod=10**9+7
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        dp=[0]*26
        for i in s:
            c=ord(i)-97
            new=ans+1-dp[c]
            ans=(ans+new)%self.mod
            dp[c]=(dp[c]+new)%self.mod
        #print(dp)
        return ans