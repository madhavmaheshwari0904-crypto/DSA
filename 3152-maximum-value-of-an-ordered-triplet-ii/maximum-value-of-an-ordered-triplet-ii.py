class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=diff=ele=0
        for i in nums:
            ans=max(ans,diff*i)
            diff=max(diff,ele-i)
            ele=max(ele,i)
        return ans