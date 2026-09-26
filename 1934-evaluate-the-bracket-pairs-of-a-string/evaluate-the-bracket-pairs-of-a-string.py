class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d=dict(knowledge)
        ans=[]
        i=0
        while(i<len(s)):
            if s[i]=='(':
                j=s.find(')',i+1)
                key=s[i+1:j]
                ans.append(d.get(key,'?'))
                i=j+1
            else:
                ans.append(s[i])
                i+=1
        return ''.join(ans)