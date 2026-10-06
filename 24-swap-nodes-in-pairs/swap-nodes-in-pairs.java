/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode head2=new ListNode();
        head2.next=head;
        ListNode prev=new ListNode();
        prev=head2;
        while(prev.next!=null && prev.next.next!=null){
            ListNode first=new ListNode();
            ListNode sec=new ListNode();
            first=prev.next;
            sec=first.next;
            first.next=sec.next;
            sec.next=first;
            prev.next=sec;
            prev=first;
        }
        return head2.next;        
    }
}