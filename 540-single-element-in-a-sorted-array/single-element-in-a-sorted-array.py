class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=1
        high=len(nums)-2
        if(len(nums)==1):
            return nums[0]
        if(nums[0]!=nums[1]):
            return nums[0]
        if(nums[len(nums)-1]!=nums[len(nums)-2]):
            return nums[len(nums)-1]    
        if(len(nums)==1):
            return nums[0]
        while(low<=high):
            mid=low+(high-low)//2
            left= (nums[mid]!=nums[mid-1])
            right=(nums[mid]!=nums[mid+1])
            if(left and right):
                return nums[mid]
            if((mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1])):
                low=mid+1
            else:
                high=mid-1    
        return -1