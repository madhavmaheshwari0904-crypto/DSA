class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans=0
        n=len(s)
        for ch in range(ord("A"),ord("Z")+1):
            i=j=r=0
            c=chr(ch)
            while(j<n):
                if s[j]==c:
                    j+=1
                elif(r<k):
                    j+=1
                    r+=1
                elif(s[i]==c):
                    i+=1
                else:
                    i+=1
                    r-=1
                ans=max(ans,j-i)
        return ans                
