class Solution(object):
    
    def expand(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """def pal(s,i,j):
            sub= s[i:j+1]
            return sub==sub[::-1]
        c=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if(pal(s,i,j)==True):
                    c+=1
        return c"""
        c = 0
        
        for i in range(len(s)):
            # Odd length palindromes 
            c += self.expand(s, i, i)
            # Even length palindromes
            c += self.expand(s, i, i + 1)
        return c