class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n=len(nums)
        ans=float('inf')
        for i in range(l,r+1):
            s=0
            for j in range(n):
                s+=nums[j]
                if j>=i:
                    s-=nums[j-i]
                if j>=i-1 and 0<s<ans:
                    ans=s
        return ans if ans!=float('inf') else -1