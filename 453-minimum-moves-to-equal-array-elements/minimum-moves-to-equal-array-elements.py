class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_=min(nums)
        return sum(i-min_ for i in nums)