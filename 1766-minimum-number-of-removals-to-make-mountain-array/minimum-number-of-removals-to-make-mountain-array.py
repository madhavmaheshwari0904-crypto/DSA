class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return 0
        n=len(nums)
        dp1=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp1[i]=max(dp1[i],dp1[j]+1)
        dp2=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j]<nums[i]:
                    dp2[i]=max(dp2[i],dp2[j]+1)
        m=0
        for i in range(1,n-1):
            if dp1[i] > 1 and dp2[i] > 1:
                curr=dp1[i]+dp2[i]-1
                m=max(curr,m)
        return n-m       