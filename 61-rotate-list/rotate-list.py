# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp=head
        prev=head
        if(head==None or head.next==None):
            return head
        n=1
        while(temp.next!=None):
            temp=temp.next
            n+=1
        k=k%n
        if(k==0):
            return head
        for i in range(n-k-1):
            prev=prev.next
        head1=prev.next
        prev.next=None
        temp.next=head
        head=head1
        return head        