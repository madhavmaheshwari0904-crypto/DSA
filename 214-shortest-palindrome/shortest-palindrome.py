class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """if not s:
            return ""
        for i in range(len(s), 0, -1):
            prefix = s[:i]
            if prefix == prefix[::-1]: 
                suffix_to_add = s[i:][::-1]
                return suffix_to_add + s

        return """""
        if not s:
            return ""
        pre=0
        suf=0
        base=29
        power=1
        mod=10**9+7
        for i,c in enumerate(s):
            char=ord(c)-ord('a')+1
            pre=(pre*base+char)%mod
            suf=(suf+char*power)%mod
            power=(power*base)%mod
            if(pre==suf):
                last=i
        suff_add=s[last+1:]
        return suff_add[::-1]+s