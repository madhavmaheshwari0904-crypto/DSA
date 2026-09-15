class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n1=len(s)
        n2=len(t)
        if(n1<n2):
            return ""
        dict1={}
        dict2={}
        ans=""
        have=0
        need=len(t)
        mini=float('inf')
        l=0
        for i in t:
            dict2[i]=dict2.get(i,0)+1
        for r in range(len(s)):
            dict1[s[r]]=dict1.get(s[r],0)+1
            if(s[r] in dict2 and dict1[s[r]]<=dict2[s[r]]):
                have+=1
            while(have==need):
                if(mini>r-l+1):
                    ans=s[l:r+1]
                    mini=r-l+1
                if s[l] in dict2 and dict1[s[l]]<=dict2[s[l]]:
                    have-=1
                dict1[s[l]]-=1
                l+=1
        return ans
