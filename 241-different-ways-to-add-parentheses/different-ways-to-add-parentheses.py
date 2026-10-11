class Solution(object):
    def solve(self,s):
        if s.isdigit():
            return [int(s)]
        ans=[]
        for i in range(len(s)):
            if s[i] in ["+","-","*"]:
                l=self.solve(s[:i])
                r=self.solve(s[i+1:])
                for j in l:
                    for k in r:
                        if s[i]=="+":ans.append(j+k)
                        if s[i]=="-":ans.append(j-k)
                        if s[i]=="*":ans.append(j*k)
        return ans

    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        return self.solve(expression)