class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=set(nums)
        i=0
        while True:
            i=i+k
            if(i not in s):
                return i
