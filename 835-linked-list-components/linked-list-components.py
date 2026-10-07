# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        c=0
        ans=set(nums)
        temp=head
        while temp:
            if temp.val in ans and (temp.next==None or temp.next.val not in ans):
                c+=1
            temp=temp.next
        return c