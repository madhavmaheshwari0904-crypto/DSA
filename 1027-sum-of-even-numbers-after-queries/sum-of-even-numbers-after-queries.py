class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        even=sum(x for x in nums if x%2==0)
        for i in queries:
            if(nums[i[1]]%2==0):
                even-=nums[i[1]]
            nums[i[1]]+=i[0]
            if nums[i[1]]%2==0:
                even+=nums[i[1]]
            ans.append(even) 
        return ans           