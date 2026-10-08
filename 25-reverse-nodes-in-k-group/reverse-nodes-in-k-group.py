# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 1:
            return head
        def reverse(temp):
            prev=None
            curr=temp
            while(curr!=None):
                t=curr.next
                curr.next=prev
                prev=curr
                curr=t
            return prev

        def getKNode(temp,k):
            while(temp!=None and k>1):
                temp=temp.next
                k-=1
            return temp
        temp=head
        prev=None
        while(temp!=None and temp.next!=None):
            kthNode=getKNode(temp,k)
            if(kthNode==None):
                if prev:
                    prev.next=temp
                break
            newNode=kthNode.next
            kthNode.next=None
            reverse(temp)
            if(temp==head):
                head=kthNode
            else:
                prev.next=kthNode
            temp.next=newNode
            prev=temp
            temp=newNode
        return head