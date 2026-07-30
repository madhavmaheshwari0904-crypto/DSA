class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while(n!=1):
            if(n%4==1 or n==3):
                n-=1
                ans+=1
            elif(n%4==3):
                n+=1
                ans+=1
            n=n//2
            ans+=1
        return ans            