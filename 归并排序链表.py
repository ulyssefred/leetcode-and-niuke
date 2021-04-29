class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortInList(self , head ):
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            prev = self
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next, prev = l1,l1
                    l1 = l1.next
                else:
                    prev.next,prev = l2, l2
                    l2 = l2.next
            prev.next = l1 if l1 is not None else l2
            return self.next
        def divide(head, tail):
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            fast = head
            slow = head
            while fast!=tail:
                fast = fast.next
                slow = slow.next
                if fast!= tail:
                    fast = fast.next
            mid = slow
            return mergeTwoLists(divide(head,mid),divide(mid,tail))
        return divide(head,None)