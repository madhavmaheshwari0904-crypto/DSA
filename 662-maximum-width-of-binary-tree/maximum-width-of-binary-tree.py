# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if root==None:
            return 0
        q=[(root,0)]
        ans=0
        while q:
            f=q[0][1]
            l=q[-1][1]
            ans=max(ans,l-f+1)
            l=[]
            for node,ind in q:
                ind-=f
                if node.left:
                    l.append((node.left,ind*2+1))
                if node.right:
                    l.append((node.right,ind*2+2))
            q=l
        return ans