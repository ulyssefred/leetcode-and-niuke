class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast = head
        slow = head
        while fast.next :
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        return slow
