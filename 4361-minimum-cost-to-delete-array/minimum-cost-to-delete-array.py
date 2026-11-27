class Solution(object):
    def minCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=nums[0]+nums[-1]
        if n==2:
            return ans
        l=nums[1:-1]
        l.sort()
        maxi=ans
        for i in range(0,n-3,2):
            maxi+=l[i]+l[i+1]
            ans=min(ans,maxi)
        return ans