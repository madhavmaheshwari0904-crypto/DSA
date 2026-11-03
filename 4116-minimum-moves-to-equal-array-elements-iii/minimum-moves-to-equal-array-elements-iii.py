class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        return sum(abs(i-m) for i in nums)