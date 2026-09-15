class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n=len(s)
        if k==1:
            return n
        ans=0
        i=0
        while(i<=n-k):
            for j in (k,k+1):
                if i+j<=n and s[i:i+j]==s[i:i+j][::-1]:
                    ans+=1
                    i+=j
                    break
            else:
                i+=1
        return ans
