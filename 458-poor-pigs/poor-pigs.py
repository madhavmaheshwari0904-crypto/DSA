class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        b=minutesToTest//minutesToDie+1
        n=1
        ans=0
        while(n<buckets):
            n*=b
            ans+=1
        return ans