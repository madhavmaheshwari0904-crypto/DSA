class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        n=len(s)
        ans=0
        d={}
        for j in range(n):
            d[s[j]]=d.get(s[j],0)+1
            while(len(d)==3):
                ans+=(n-j)
                d[s[i]]-= 1
                if(d[s[i]]==0):
                    del d[s[i]]
                i+=1
        return ans            