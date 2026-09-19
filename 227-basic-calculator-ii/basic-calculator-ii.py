class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        l=0
        sign='+'
        c=0
        for i,char in enumerate(s):
            if(char.isdigit()):
                c=c*10+int(char)
            if (not char.isspace() and not char.isdigit()) or i == len(s) - 1:
                if sign in ('+','-'):
                    ans+=l
                    l=c if sign=='+'else -c
                elif sign == '*':
                    l=l*c
                elif sign == '/':
                    l=int(float(l)/c)
                sign = char
                c = 0
        ans+=l
        return ans
