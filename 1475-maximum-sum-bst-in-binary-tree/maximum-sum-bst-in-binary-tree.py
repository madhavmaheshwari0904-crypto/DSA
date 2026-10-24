# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode | None) -> int:
        ans=0
        def dfs(root):
            if root==None:
                return inf,-inf,0
            l_min,l_max,l_sum=dfs(root.left)
            r_min,r_max,r_sum=dfs(root.right)
            v=root.val
            if v<=l_max or v>=r_min:
                return -inf,inf,0
            s=l_sum+r_sum+v
            nonlocal ans
            ans=max(ans,s)
            return min(l_min,v),max(r_max,v),s
        dfs(root)
        return ans