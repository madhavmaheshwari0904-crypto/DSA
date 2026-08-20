class Solution(object):
    def fun(self,bloomDay,mid,m,k):
        c=0
        bouquets=0
        for i in bloomDay:
            if(i<=mid):
                c+=1
                if(c==k):
                    bouquets+=(c//k)
                    c=0
            else:
                c=0
        if(bouquets>=m):
            return True
        else:
            return False 
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """           
        n=len(bloomDay)
        if(m*k>n):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            total=self.fun(bloomDay,mid,m,k)
            if(total):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans            