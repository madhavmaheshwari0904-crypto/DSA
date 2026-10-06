# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s=0
        while(head!=None):
            s=s*10 +head.val
            head=head.next
        head1=ListNode(0)
        curr=head1
        s=s*2
        for i in str(s):
            head1.next=ListNode(int(i))
            head1=head1.next
        return curr.next