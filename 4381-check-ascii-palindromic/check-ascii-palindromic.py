class Solution(object):
    def isPalindromic(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans=""
        for i in s:
            ans+=format(ord(i),'08b')
        print(ans)    
        return ans==ans[::-1]    