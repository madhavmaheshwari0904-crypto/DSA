import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        r=max(piles)
        l=1
        ans=r
        while(l<=r):
            mid=(l+r)//2
            s=0
            for i in piles:
                s+=math.ceil(float(i)/mid)
            if s<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans