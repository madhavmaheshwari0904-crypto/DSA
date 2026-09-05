class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        small=[0]*n
        l=nums[0]
        m=nums[n-1]
        for i in range(n-1,-1,-1):
            m = min(m,nums[i])
            small[i] = m
        for i in range(n):
            l=max(l,nums[i])
            if(l-small[i]<=k):
                return i
        return -1        
