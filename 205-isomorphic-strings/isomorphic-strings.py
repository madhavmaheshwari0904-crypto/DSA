class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=set(s)
        t1=set(t)
        return len(s1)==len(t1)==len(set(zip(s,t)))