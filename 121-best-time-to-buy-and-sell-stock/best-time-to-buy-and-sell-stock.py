class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """l=0
        r=1
        p=0
        while(r<len(prices)):
            c=prices[r]-prices[l]
            if(prices[l]<prices[r]):
                p=max(p,c)
            else:
                l=r
            r+=1
        return p       """
        if len(prices) == 1:
            return 0
        minP = prices[0]
        maxPro = 0
        for i in  prices:
            minP = min(i, minP)
            maxPro = max(i-minP, maxPro)
        return maxPro