class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==1):
            return nums[-1]
        c=0
        m=float('-inf')
        for i in nums:
            c+=i
            m=max(m,c)
            if(c<0):
                c=0
        return m         