class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        s=sum(cardPoints[:k])
        m=s
        n=len(cardPoints)
        for i in range(1,k+1):
            s=s-cardPoints[k-i]+cardPoints[n-i]
            m=s if s>m else m
        return m    