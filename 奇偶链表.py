class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = head
        even = head.next
        evenhead = head.next
        while even and even.next:
            odd.next, odd = even.next, even.next
            even.next,even = odd.next, odd.next
        odd.next = evenhead
        return head