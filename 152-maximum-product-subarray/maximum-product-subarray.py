class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=max(nums)
        curr_max=1
        curr_min=1
        for i in nums:
            temp=curr_max*i
            curr_max=max(temp,curr_min*i,i)
            curr_min=min(temp,curr_min*i,i)
            ans=max(ans,curr_max)
        return ans    