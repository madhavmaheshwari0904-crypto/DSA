class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mini=ans=nums[k]
        i=j=k
        n=len(nums)
        while(i>0 or j<n-1):
            if(i==0):
                j+=1
            elif(j==n-1):
                i-=1
            elif(nums[i-1]<nums[j+1]):
                j+=1
            else:
                i-=1
            mini=min(mini,nums[i],nums[j])
            ans=max(ans,mini*(j-i+1))
        return ans        