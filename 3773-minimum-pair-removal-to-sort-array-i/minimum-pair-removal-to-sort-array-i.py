class Solution(object):
    def minimumPairRemoval(self, nums):
        count=0
        
        def check(nums):
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    return False
            return True
        while not check(nums):
            mini=float('inf')
            for i in range(1,len(nums)):
                if (nums[i]+nums[i-1])<mini:
                    mini=(nums[i]+nums[i-1])
                    index=i
            nums[index-1]+=nums[index]
            nums.pop(index)
            count+=1
        return count    