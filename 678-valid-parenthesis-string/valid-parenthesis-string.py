class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sum_p=0
        l=0
        for i in range(0,len(s)):
            if(s[i]=="("):
                sum_p+=1
                l=l+1
            elif(s[i]==")"):
                sum_p-=1
                l=max(l-1,0)
            else:
                l=max(l-1,0)
                sum_p+=1
            if(sum_p<0):
                return False            
        return l==0