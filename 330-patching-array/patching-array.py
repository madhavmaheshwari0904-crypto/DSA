class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss=1
        ans=0
        idx=0
        while miss<=n:
            if idx<len(nums) and nums[idx]<=miss :
                miss+=nums[idx]
                idx+=1
            else:
                miss+=miss
                ans+=1
        return ans