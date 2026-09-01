class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        t=[]
        for i in range(len(nums)):
            t.insert(index[i],nums[i])
        return t
        