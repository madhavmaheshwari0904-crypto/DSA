# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def make():
            node=TreeNode(postorder.pop())
            if node.val !=preorder[-1]:
                node.right=make()
            if node.val!=preorder[-1]:
                node.left=make()
            preorder.pop()
            return node
        return make()