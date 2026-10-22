# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def parent(node,par):
            if node is None:
                return
            d[node]=par
            parent(node.left,node)
            parent(node.right,node)
        def solve(node,dis):
            if not node or node in vis or dis>k:
                return 
            vis.add(node)
            if dis==k:
                ans.append(node.val)
            solve(node.left,dis+1)
            solve(node.right,dis+1)
            solve(d[node],dis+1)
        d={}
        vis=set()
        ans=[]
        parent(root,None)
        solve(target,0)
        return ans