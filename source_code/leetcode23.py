def mergeKLists(lists):
    def mergeTwoLists(l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head=ListNode()
        cur=head
        while l1 and l2:
                val1=l1.val
                val2=l2.val
                if val1>=val2:
                    cur.next=l2
                    l2=l2.next
                if val2>val1:
                    cur.next=l1
                    l1=l1.next
                cur=cur.next
        if l1:
            cur.next=l1
        if l2:
            cur.next=l2
        return head.next

    while len(lists)>1:
        ans=[]
        while len(lists)>1:
            l1=lists.pop()
            l2=lists.pop()
            ans.append(mergeTwoLists(l1,l2))
        ans.extend(lists)
        lists=ans
    if lists:
        return lists[0]
    else:
        return None
