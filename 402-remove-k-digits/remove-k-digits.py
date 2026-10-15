class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        s=[]
        for i in num:
            while k > 0 and s and s[-1] > i:
                s.pop()
                k -= 1
            s.append(i)
        if k>0:
            s=s[:-k]
            print(s)
        ans="".join(s).lstrip("0")
        return ans if ans else "0"