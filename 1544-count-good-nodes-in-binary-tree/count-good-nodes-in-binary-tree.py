# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def solve(root,maxi):
            if root==None:
                return 0
            c=1 if root.val>=maxi else 0
            maxi=max(maxi,root.val)
            c+=solve(root.left,maxi)
            c+=solve(root.right,maxi)
            return c
        return solve(root,root.val)