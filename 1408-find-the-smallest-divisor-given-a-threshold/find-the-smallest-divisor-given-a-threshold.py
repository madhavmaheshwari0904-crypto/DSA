class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def solve(div):
            return sum((i + div - 1) // div for i in nums)
        low=1
        high=max(nums)
        res=0
        while(low<=high):
            mid=(low+high)//2
            ans=solve(mid)
            if(ans<=threshold):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res                