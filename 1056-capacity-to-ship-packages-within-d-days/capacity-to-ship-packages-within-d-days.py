class Solution(object):
    def solve(self,weights,mid,days):
        w=0
        c=1
        for i in weights:
            if(i+w>mid):
                c+=1
                w=i
            else:
                w+=i    
        return c<=days    
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        high=sum(weights)
        low=max(weights)
        ans=high
        while(low<=high):
            mid=(low+high)//2
            if(self.solve(weights,mid,days)):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans            