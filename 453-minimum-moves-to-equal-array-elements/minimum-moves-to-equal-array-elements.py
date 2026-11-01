class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_=min(nums)
        return sum(nums)-min_*len(nums)