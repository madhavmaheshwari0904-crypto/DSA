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
    public ListNode reverseList(ListNode head) {
        ListNode temp=new ListNode();
        ListNode curr=new ListNode();
        ListNode prev=new ListNode();
        temp=head;
        curr=temp;
        prev=null;
        while(temp !=null){
            temp=temp.next;
            curr.next=prev;
            prev=curr;
            curr=temp;
        }
        return prev;
    }
}