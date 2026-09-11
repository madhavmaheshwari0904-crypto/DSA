class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        c=0
        p=permutations(digits,3)
        ans=[100*i+10*j+k for i,j,k in p if(i!=0)]
        ans=set(ans)
        for i in ans:
            if(i%2==0):
                c+=1
        return c        
        