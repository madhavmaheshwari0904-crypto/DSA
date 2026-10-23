class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=-1
        for i,val in enumerate(nums):
            if i!=val:
                k&=i
        return 0 if k==-1 else k