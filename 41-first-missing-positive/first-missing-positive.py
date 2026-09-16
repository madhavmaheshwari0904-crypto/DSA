class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        r=1
        for i in nums:
            if(i==r):
                r+=1
        return r     