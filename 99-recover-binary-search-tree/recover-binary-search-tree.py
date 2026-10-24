# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.prev=None
        self.f=None
        self.sec=None
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def solve(root):
            if root==None:
                return
            solve(root.left)
            if(self.prev!=None and self.prev.val>root.val):
                if self.f==None:
                    self.f=self.prev
                self.sec=root
            self.prev=root
            solve(root.right)
        solve(root)
        t=self.f.val
        self.f.val=self.sec.val
        self.sec.val=t