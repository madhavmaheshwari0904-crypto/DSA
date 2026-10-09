class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        stack=[]
        i=0
        while i<len(s):
            if s[i]=='(':
                stack.append(s[i])
            else:
                if not stack:
                    if i<len(s)-1 and s[i+1]==')':
                        i+=1
                    else:
                        ans+=1
                    ans+=1
                else:
                    if i<len(s)-1 and s[i+1]==')':
                        i+=1
                    else:
                        ans+=1
                    stack.pop()
            i+=1
        return ans+len(stack)*2