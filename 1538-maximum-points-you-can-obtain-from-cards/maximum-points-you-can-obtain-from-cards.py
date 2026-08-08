class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if len(cardPoints)==k:
            return sum(cardPoints)
        t=sum(cardPoints)
        n=len(cardPoints)
        r=n-k
        sub=sum(cardPoints[:r])
        m=sub
        for i in range(r,n):
            sub+=cardPoints[i]
            sub-=cardPoints[i-r]
            m=min(m,sub)
        return t-m    