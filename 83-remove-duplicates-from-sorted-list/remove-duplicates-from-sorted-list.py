# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:
            return head
        prev=head
        temp=head.next
        while(temp!=None):
            if(prev.val!=temp.val):
                prev.next=temp
                prev=prev.next
            temp=temp.next
        prev.next=None
        return head