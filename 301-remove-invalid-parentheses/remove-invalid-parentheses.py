class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left=0
        right=0
        for i in s:
            if i=='(':
                left+=1
            if i==')':
                if left>0:
                    left-=1
                else:
                    right+=1
        ans=set()
        def solve(i,left,right,bal,path):
            if i==len(s):
                if left==0 and right == 0 and bal == 0:
                    ans.add(''.join(path))
                return 
            ch=s[i]
            if ch=='(':
                if left>0:
                    solve(i+1,left-1,right,bal,path)
                path.append(ch)
                solve(i+1,left,right,bal+1,path)
                path.pop()
            elif ch==')':
                if right>0:
                    solve(i+1,left,right-1,bal,path)
                if bal>0:
                    path.append(ch)
                    solve(i+1,left,right,bal-1,path)
                    path.pop()
            else:
                path.append(ch)
                solve(i + 1, left, right, bal, path)
                path.pop()
        solve(0,left,right,0,[])
        return list(ans)

                
