class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==1 or n==7):
            return True
        elif(n<10):
            return False
        else:
            s=0
            while n>0:
                t=n%10
                s=s+t**2
                n=n//10
            return self.isHappy(s)            