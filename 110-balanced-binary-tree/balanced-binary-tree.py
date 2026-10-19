# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def solve(root):
            if root==None:
                return 0
            l=solve(root.left)
            r=solve(root.right)
            if(l==-1 or r==-1):
                return -1
            if abs(l-r)>1:
                return -1
            return 1+max(l,r)
        if root==None:
            return True
        if solve(root)==-1:
            return False
        return True
