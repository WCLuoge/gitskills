def swapParis(head):
    if head==None or head.next==None:
        return head
    newhead=ListNode()
    cur=newhead
    while head:
        first=head
        cur.next=first
        head=head.next
        first.next=None
        if head==None:
            break
        second=head
        head=head.next
        second.next=first
        cur.next=second
        cur=first
    return newhead.next
