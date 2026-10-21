class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=sorted(s)
        if list(s)==ans:
            return 0
        if len(s)<=2:
            return -1
        if (ans[0]==s[-1] and ans[1]!=ans[0])and (ans[-1]==s[0] and ans[-1]!=ans[-2]):
            return 3
        elif ans[0]==s[0] or ans[-1]==s[-1]:
            return 1
        else:
            return 2
        