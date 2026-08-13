class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        m=0
        ans=0
        for k in range(len(nums)-1):
            m=max(m,k+nums[k])
            if(m>=len(nums)-1):
                ans+=1
                break
            if(k==j):
                ans+=1
                j=m
        return ans        