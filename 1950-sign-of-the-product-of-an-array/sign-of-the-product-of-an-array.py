class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=1
        for i in nums:
            p*=i
        if p<0:
            return -1
        if p>0:
            return 1
        else:
            return 0