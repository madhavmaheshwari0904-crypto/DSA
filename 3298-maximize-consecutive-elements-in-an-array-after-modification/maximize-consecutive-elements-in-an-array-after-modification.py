class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mx=nums[-1]
        dp=[0]*(mx+2)
        ans=1
        #print(dp)
        for i in nums:
            dp[i+1]=dp[i]+1
            dp[i]=dp[i-1]+1
            ans=max(ans,dp[i],dp[i+1])
            #print(dp)
        return ans
