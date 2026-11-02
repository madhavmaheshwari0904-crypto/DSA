class Solution(object):
    def minMergedInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=float('inf')
        i=0
        j=1
        while j<len(nums):
            m=min(m,int(str(nums[i])+str(nums[j])))
            i+=2
            j+=2
        return m