# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        self.nodes=[]
        def view(root,row,col):
            if root==None:
                return 
            self.nodes.append((col,row,root.val))
            view(root.left,row+1,col-1)
            view(root.right,row+1,col+1)
        view(root,0,0)
        self.nodes.sort()
        #print(self.nodes)
        ans=[]
        prev=float('inf')
        for col,row,num in self.nodes:
            if col!=prev:
                ans.append([])
                prev=col
            ans[-1].append(num)
        return ans
