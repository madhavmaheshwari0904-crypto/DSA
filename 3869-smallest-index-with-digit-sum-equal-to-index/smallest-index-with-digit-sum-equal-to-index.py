class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sum(i):
            s=0
            while(i!=0):
                s+=(i%10)
                i/=10
            return s    
        for i in range(len(nums)):
            if i==sum(nums[i]):
                return i
        return -1        