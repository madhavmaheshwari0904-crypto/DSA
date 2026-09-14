class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i=j=s=0
        mini=float('inf')
        while(j<len(nums)):
            s+=nums[j]
            while(s>=target):
                s-=nums[i]
                mini=min(mini,j-i+1)
                i+=1
            j+=1
        if mini==float('inf'):
            return 0
        return mini