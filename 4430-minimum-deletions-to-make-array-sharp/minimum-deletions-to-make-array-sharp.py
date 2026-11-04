class Solution(object):
    def minDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(a == b for a, b in zip(nums, nums[1:]))
