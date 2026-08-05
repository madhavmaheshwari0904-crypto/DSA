class Solution(object):
    def lastStoneWeight(self, nums):
        """
        :type stones: List[int]
        :rtype: int
        """
        while(len(nums)>=2):
            nums.sort()
            a=nums.pop()
            b=nums.pop()
            if(a>b):
                nums.append(a-b)
        return nums[0] if len(nums) else 0        
        