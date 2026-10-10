class Solution(object):
    def mergeAlternately(self, s, t):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        j = 0
        ans = ""
        while i < len(s) and j < len(t):
            ans += s[i]
            ans += t[j]
            i += 1
            j += 1
        while i < len(s):
            ans += s[i]
            i += 1
        while j < len(t):
            ans += t[j]
            j += 1
        return ans