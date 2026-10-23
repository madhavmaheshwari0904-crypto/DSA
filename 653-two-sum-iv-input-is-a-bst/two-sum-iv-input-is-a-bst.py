# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.s=set()
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        if root==None:
            return False
        if k-root.val in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left,k) or self.findTarget(root.right,k)