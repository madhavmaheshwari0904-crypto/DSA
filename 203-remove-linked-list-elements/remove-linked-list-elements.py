# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        """if(head==None):
            return None
        head.next=self.removeElements(head.next, val)
        return head.next if(head.val==val) else head"""
        while head and head.val == val:
            head = head.next
        curr=head
        while curr and curr.next:
            if(curr.next.val==val):
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head