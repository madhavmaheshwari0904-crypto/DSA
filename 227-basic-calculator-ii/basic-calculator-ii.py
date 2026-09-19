class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        sign='+'
        c=0
        for i,char in enumerate(s):
            if(char.isdigit()):
                c=c*10+int(char)
            if (not char.isspace() and not char.isdigit()) or i == len(s) - 1:
                if sign == '+':
                    l.append(c)
                elif sign == '-':
                    l.append(-c)
                elif sign == '*':
                    l.append(l.pop() * c)
                elif sign == '/':
                    prev = l.pop()
                    l.append(int(float(prev) / c))
                sign = char
                c = 0
        return sum(l)
