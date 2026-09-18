class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        dp=[0]*(k+1)
        print(dp)
        ans=0
        while(dp[k]<n):
            for i in range(k,0,-1):
                dp[i]=dp[i]+dp[i-1]+1
            ans+=1
            print(dp)
            print(ans)
        return ans