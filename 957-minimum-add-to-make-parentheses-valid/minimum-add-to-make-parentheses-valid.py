class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans=0
        miss=0
        for i in s:
            if(i=='('):
                ans+=1
            else:
                if(ans>0):
                    ans-=1
                else:
                    miss+=1
        return ans + miss