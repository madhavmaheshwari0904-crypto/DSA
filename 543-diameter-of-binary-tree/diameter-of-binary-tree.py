# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #m=[0]
        def height(root):
            if(root==None):
                return 0,0
            l_h,l=height(root.left)
            r_h,r=height(root.right)
            #m[0]=max(m[0],l+r)
            return max(l_h,r_h)+1,max(l,r,l_h+r_h)
        #height(root)
        _,dia=height(root)
        return dia
        