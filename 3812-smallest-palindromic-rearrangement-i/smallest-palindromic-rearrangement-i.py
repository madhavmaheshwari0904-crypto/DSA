class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)//2
        start="".join(sorted(s[:n]))
        print(start)
        if(len(s)%2!=0):
            mid=s[n]
        else:
            mid=""
        return start+mid+start[::-1]        