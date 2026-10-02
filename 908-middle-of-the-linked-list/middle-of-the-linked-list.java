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
    public ListNode middleNode(ListNode head) {
        ListNode temp=new ListNode();
        temp=head;
        int n=0;
        while(temp!=null){
            temp=temp.next;
            n+=1;
        }
        temp=head;
        n=n/2;
        while(n>0){
            temp=temp.next;
            n-=1;
        }
        return temp;
    }
}