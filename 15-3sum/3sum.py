class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """ans=[]
        nums.sort()
        for i in range(len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                s=nums[i]+nums[j]+nums[k]
                if(s>0):
                    k=k-1
                elif(s<0):
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    while(j<k and nums[j]==nums[j+1]):
                        j=j+1
                    while(j<k and nums[k]==nums[k-1]):
                        k-=1   
                    j+=1
                    k-=1     
        return ans       """
        """nums.sort()
        ans=set()
        for i in range(len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            for j in range(i+1,len(nums)-1):
                t=0-(nums[i]+nums[j])
                if t in nums:
                    ans.add((nums[i],nums[j],t))  
        return [list(i) for i in ans]    """
        nums.sort()
        ans = set()
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            seen = set()
            for j in range(i + 1, n):
                target = -(nums[i] + nums[j])
                
                if target in seen:
                    ans.add((nums[i], target, nums[j]))
                else:
                    seen.add(nums[j])
                    
        return [list(triplet) for triplet in ans]       
