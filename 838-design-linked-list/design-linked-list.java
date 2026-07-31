class MyLinkedList {
    class Node {
        int val;
        Node next;
        Node(int val) {
            this.val = val;
            this.next = null;
        }
    }
    
    Node head;
    Node tail;
    int l;

    public MyLinkedList() {
        head = null;
        tail = null;
        l = 0;
    }
    
    public int get(int index) {
        if (index < 0 || index >= l || head == null) return -1;
        
        Node temp = head;
        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp.val;
    }
    
    public void addAtHead(int val) {
        Node newNode = new Node(val);
        if (head == null) {
            head = tail = newNode;
        } else {
            newNode.next = head;
            head = newNode;
        }
        l++;
    }
    
    public void addAtTail(int val) {
        Node newTail = new Node(val);
        if (tail == null) {
            head = tail = newTail;
        } else {
            tail.next = newTail;
            tail = newTail;
        }
        l++; 
    }
    
    public void addAtIndex(int index, int val) {
        if (index < 0 || index > l) return;
        
        if (index == 0) {
            addAtHead(val);
        } else if (index == l) {
            addAtTail(val);
        } else {
            Node newNode = new Node(val);
            Node temp = head;
            for (int i = 0; i < index - 1; i++) {
                temp = temp.next;
            }
            newNode.next = temp.next;
            temp.next = newNode;
            l++;
        }
    }
    
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= l || head == null) return;
        
        if (head == tail) {
            head = tail = null;
            l--;
        } else if (index == 0) {
            head = head.next;
            l--;
        } else if (index == l - 1) {
            Node temp = head;
            while (temp.next != tail) {
                temp = temp.next;
            }
            temp.next = null;
            tail = temp;
            l--;
        } else {
            Node temp = head;
            for (int i = 0; i < index - 1; i++) {
                temp = temp.next;
            }
            temp.next = temp.next.next;
            l--;
        }    
    }
}