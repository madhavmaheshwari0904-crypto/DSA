class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l=sorted(i*i for i in nums)
        print(l)
        return sum(l[n//2:])-sum(l[:n//2])
        