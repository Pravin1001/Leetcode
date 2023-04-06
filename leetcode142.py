class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=set()
        while head:
            if head in temp:
                return head
            temp.add(head)
            head=head.next
        return None
