class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        n=sorted(nums)[len(nums)//2]
        for i in nums:
            c=c+abs(n-i)
        return c    