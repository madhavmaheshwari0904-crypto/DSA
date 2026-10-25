class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:return nums[0]
        def fin(nums,s,e):
            dp=[-1]*n
            return solve(nums,s,e,dp)
        def solve(nums,s,e,dp):
            if s>e:
                return 0
            if dp[s]!=-1:return dp[s]
            take=nums[s]+solve(nums,s+2,e,dp)
            not_take=solve(nums,s+1,e,dp)
            dp[s]=max(take,not_take)
            return dp[s]
        f=fin(nums,0,n-2)
        s=fin(nums,1,n-1)
        return max(f,s)