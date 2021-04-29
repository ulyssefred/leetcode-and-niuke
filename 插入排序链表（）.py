class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = self
        pre.next = head
        cur = head.next
        last = head
        while cur:
            if last.val <= cur.val:
                last = last.next
            else:
                pre = self
                while pre.next.val <= cur.val:
                    pre = pre.next
                last.next, cur.next, pre.next = cur.next, pre.next, cur
            cur = last.next
        return self.next

