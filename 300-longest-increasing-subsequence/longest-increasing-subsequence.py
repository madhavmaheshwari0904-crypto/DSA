class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """def solve(i,prev,dp):
            if i>=len(nums):
                return 0
            ind=prev+1
            if dp[i][ind]!=-1:
                return dp[i][ind]
            not_take=0+solve(i+1,prev,dp)
            take=0
            if nums[prev]<nums[i] or prev==-1:
                prev=i
                take=1+solve(i+1,prev,dp)
            dp[i][ind]= max(not_take,take)
            return dp[i][ind]
        dp=[[-1]*(len(nums)+1) for _ in range(len(nums))]
        return solve(0,-1,dp)"""
        if  not nums:
            return 0
        n=len(nums)
        dp=[1]*n
        for i in range(1,n):
            for j in range(i) :
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)