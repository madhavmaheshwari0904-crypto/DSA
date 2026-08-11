class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        s=nums[0]
        while(i<len(nums) and nums[i-1]+1==nums[i]):
            s+=nums[i]
            i+=1
        while True:
            if(s not in nums):
                return s
            s+=1    

