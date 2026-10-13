class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """l=len(nums)
        if(l==0):
            return []
        s=[-1]*l
        for i in range(0,l):
            for j in range(1,l):
                p=(i+j)%l
                if(nums[i]<nums[p]):
                    s[i]=nums[p]
                    break
        return s  """
        s=[]
        n=len(nums)
        ans=[-1]*n 
        for i in range(2*n-1,-1,-1):
            while(s and s[-1]<=nums[i%n]):
                s.pop()
            if i<n and s:
                ans[i]=s[-1]
            s.append(nums[i%n])
        return ans