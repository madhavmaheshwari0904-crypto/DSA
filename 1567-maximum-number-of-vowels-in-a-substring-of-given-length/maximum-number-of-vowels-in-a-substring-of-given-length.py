class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        v='aeiou'
        temp=sum(1 for i in s[:k] if i in v)
        ans=temp
        for i in range(k,len(s)):
            if s[i] in v:
                temp+=1
            if s[i-k] in v:
                temp-=1
            ans=max(ans,temp)
        return ans            