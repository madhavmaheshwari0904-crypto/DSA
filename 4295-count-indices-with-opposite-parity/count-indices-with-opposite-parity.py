class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            s=0
            for j in range(i+1,len(nums)):
                if(nums[i]%2==0 and nums[j]%2!=0):
                    s+=1
                if(nums[j]%2==0 and nums[i]%2!=0):
                    s+=1
            ans.append(s)
        return ans                