class Solution(object):
    def solve(self,s):
        if s.isdigit():
            return [int(s)]
        if s in self.dp:
            return self.dp[s]
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
        self.dp[s]=ans
        return ans

    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        self.dp={}
        return self.solve(expression)