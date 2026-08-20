class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1=[]
        l1.append(nums[0])
        l2=[]
        l2.append(nums[1])
        for i in range(2,len(nums)):
            if(l1[-1]>l2[-1]):
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        return l1+l2            
